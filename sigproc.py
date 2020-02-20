#Amélia's signal processing module
#Use wisely. Be amazing. Make awesome stuff. ^w^

#Copyright (c) 2020 Amélia O. F da S.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#This module was made because I'm not sure scipy is supported on circuitpython
#If it is, please use scipy.signal instead of this

#Math is important.
import math

#Maps outputs to the -amplitude ~ amplitude range (e.g.: normalize([50,0,-50,25],1) == [1,0,-1,.5])
def normalize(samples,amplitude=1):
    max=0
    min=0
    for sample in samples:
        max=sample if sample>max else max
        min=sample if sample<min else min
    return [(-amplitude)+(((sample-min)/(max-min))*2*amplitude) for sample in samples]

#Removes DC offset with exponential average (frequency parameter is used for fine-tuning the average for a certain oscillation width)
def clearDCOffset(samples,srate=2048):
    avg=samples[0]
    #Exp. Avg. decay parameter. It should be slow-decaying. Sorry, but this was determined by trial-and-error.
    w=math.sqrt(1/srate)
    w=2 if w==0 else w
    ret=[]
    for sample in samples:
        avg=avg+(sample-avg)*w
        ret.append(sample-avg)
    return ret

#Calculates an envelope of a signal (frequency parameter is used for fine-tuning. See clearDCOffset)
def envelope(samples,srate=2048):
    samples=[abs(sample) for sample in samples]
    avg=samples[0]
    #Exp. Avg. decay parameter. It should be slow-decaying. Sorry, but this was determined by trial-and-error.
    w=math.sqrt(1/srate)**1.50
    w=2 if w==0 else w
    ret=[]
    for sample in samples:
        avg=avg+(sample-avg)*w
        ret.append(avg)
    return ret

#Returns the sum of all samples on a signal.
#One can see it (though it's not really 100% right) as an integral
def sum(samples):
    acc=0
    for sample in samples:
        acc+=sample
    return acc

#https://en.wikipedia.org/wiki/High-pass_filter
#Input: array(samples), float(cutoff):cutoff freq., float(srate):sampling rate
def highpass(samples,cutoff,srate):
    rc=1/(2*math.pi*cutoff) #RC time constant
    dt=1/srate #Delta-time
    alpha=rc/(rc+dt)
    y=[samples[0]]
    for i in range(1,len(samples)):
        y.append(alpha*(y[i-1]+samples[i]-samples[i-1]))
    return y
#https://en.wikipedia.org/wiki/Low-pass_filter
#TODO: https://en.wikipedia.org/wiki/Butterworth_filter
#Input: array(samples), float(cutoff):cutoff freq., float(srate):sampling rate
def lowpass(samples,cutoff,srate):
    rc=1/(2*math.pi*cutoff) #RC time constant
    dt=1/srate #Delta-time
    alpha=rc/(rc+dt)
    y=[alpha*samples[0]]
    for i in range(1,len(samples)):
        y.append(y[i-1]+alpha*(samples[i]-y[i-1]))
    return y

#calculates the high/low ratio based on a cutoff frequency
def hlratio(samples,cutoff,srate):
    HP=highpass(samples,cutoff,srate)
    HP=sum(envelope(HP,srate))
    LP=lowpass(samples,cutoff,srate)
    LP=sum(envelope(LP,srate))
    return HP/LP