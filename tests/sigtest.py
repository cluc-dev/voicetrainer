import math
import matplotlib.pyplot as plt
import sigproc
import simpleaudio as sa
import numpy as np

#A simple program demonstrating the usage of the sigproc module

SR=16000
X=range(0,SR)

#We have a constant signal at 200hz
S=[math.sin(200*((x*2*math.pi)/SR)) for x in X]
#Another one at 1100hz
S=[s+math.sin(1100*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]
#And yet another one at 2000hz
S=[s+math.sin(2000*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]

#If we choose a cutoff frequency of 800, for example
#the highpass-filtered signal should yield a higher envelope than the lowpass-filtered one
cutoff=800

#Even though we built this wave from pure sine waves, and therefore it's already aligned to the 0-axis,
#I'll leave this line here so people can understand it in the future.
DC=sigproc.clearDCOffset(S,SR)

#We create two new arrays: a thrice highpass-filtered signal and a thrice lowpass-filtered one
HP=sigproc.highpass(DC,cutoff,SR)
HP=sigproc.highpass(HP,cutoff,SR)
HP=sigproc.highpass(HP,cutoff,SR)
LP=sigproc.lowpass(DC,cutoff,SR)
LP=sigproc.lowpass(LP,cutoff,SR)
LP=sigproc.lowpass(LP,cutoff,SR)

#Envelopes
DCE=sigproc.envelope(DC,SR)
HPE=sigproc.envelope(HP,SR)
LPE=sigproc.envelope(LP,SR)

print("High/Low ratio: "+str(sigproc.sum(HPE)/sigproc.sum(LPE)))

plt.plot(X,DCE,'k')
plt.plot(X,HPE,'r')
plt.plot(X,LPE,'b')
plt.show()

DC=np.array([int(s) for s in sigproc.normalize(DC,(2**14)-1)]).astype(np.int16)
HP=np.array([int(s) for s in sigproc.normalize(HP,(2**14)-1)]).astype(np.int16)
LP=np.array([int(s) for s in sigproc.normalize(LP,(2**14)-1)]).astype(np.int16)
#Let's play the sounds
sa.play_buffer(DC,1,2,SR)
plt.plot(X,DCE,'y')
plt.show()
sa.play_buffer(HP,1,2,SR)
plt.plot(X,HPE,"m")
plt.show()
sa.play_buffer(LP,1,2,SR)
plt.plot(X,LPE,"b")
plt.show()
