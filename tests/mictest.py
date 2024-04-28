import sounddevice as sd
import math
import matplotlib.pyplot as plt
import sigproc

SR=160000
duration = 10
SIG = sd.rec(duration * SR, samplerate=SR, channels=2,dtype='float64')
print("Recording...")
sd.wait()
print("Processing...")

SIG=[s[0] for s in SIG]

step=math.floor(SR/8)
fs=range(0,len(SIG)-step,step)
ratio=[]
cutoff=350
for i in fs:
    ratio.append(sigproc.hlratio(SIG[i:i+step-1],cutoff,SR))
plt.xlabel("Time(s)")
plt.ylabel("High/Low ratio")
plt.plot([s/SR for s in fs],ratio)
plt.show()
sd.play(SIG, SR)
sd.wait()
print("OK")