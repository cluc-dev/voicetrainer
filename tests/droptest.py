import math
import matplotlib.pyplot as plt
import sigproc
import simpleaudio as sa
import numpy as np

SR=16000
X=range(0,SR)

#Our signal
SIG=[]

#Normal condition
#We have a constant signal at 200hz
S=[math.sin(200*((x*2*math.pi)/SR)) for x in X]
#Another one at 1100hz
S=[s+math.sin(1100*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]
#And yet another one at 2000hz
S=[s+math.sin(2000*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]

#Drop condition
#We have a constant signal at 200hz
D=[math.sin(200*((x*2*math.pi)/SR)) for x in X]
#Another one at 1100hz
D=[s+math.sin(600*((x*2*math.pi)/SR)) for (x,s) in enumerate(D)]
#And yet another one at 2000hz
D=[s+math.sin(1500*((x*2*math.pi)/SR)) for (x,s) in enumerate(D)]

#We build a SIG with 3 sections: normal, drop, normal
SIG.extend(S)
SIG.extend(D)
SIG.extend(S)

step=math.floor(SR/8)
fs=range(0,len(SIG)-step,step)
ratio=[]
cutoff=1000
for i in fs:
    ratio.append(sigproc.hlratio(SIG[i:i+step-1],cutoff,SR))
plt.xlabel("Time(s)")
plt.ylabel("High/Low ratio")
plt.plot([s/SR for s in fs],ratio)
plt.show()