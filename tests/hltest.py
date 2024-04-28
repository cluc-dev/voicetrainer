import math
import matplotlib.pyplot as plt
import sigproc
import simpleaudio as sa
import numpy as np

SR=16000
X=range(0,SR)

#We have a constant signal at 200hz
S=[math.sin(200*((x*2*math.pi)/SR)) for x in X]
#Another one at 1100hz
S=[s+math.sin(1100*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]
#And yet another one at 2000hz
S=[s+math.sin(2000*((x*2*math.pi)/SR)) for (x,s) in enumerate(S)]

fs=range(200,2000,200)
ratio=[]
for i in fs:
    ratio.append(sigproc.hlratio(S,i,SR))
plt.xlabel("Cutoff Frequency")
plt.ylabel("High/Low ratio")
plt.plot(fs,ratio)
plt.show()