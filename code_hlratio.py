import time
import array
import board
import audiobusio
import simpleio
import neopixel
import sigproc

#---| User Configuration |---------------------------
SAMPLERATE = 16000
SAMPLES = 4000
THRESHOLD = 100
MIN_DELTAS = 30
DELAY = 0.4

#your target voice hlratio (determine this experimentally/make a callibration feature)
RATIO_TARGET = 0.8

#Preferably a midpoint between your "low" and "high" frequencies
CUTOFF=350

COLORS = (
    (0xFF, 0x00, 0x00) , # pixel 0
    (0xFF, 0x71, 0x00) , # pixel 1
    (0xFF, 0xE2, 0x00) , # pixel 2
    (0xAA, 0xFF, 0x00) , # pixel 3
    (0x38, 0xFF, 0x00) , # pixel 4
    (0x00, 0xFF, 0x38) , # pixel 5
    (0x00, 0xFF, 0xA9) , # pixel 6
    (0x00, 0xE2, 0xFF) , # pixel 7
    (0x00, 0x71, 0xFF) , # pixel 8
    (0x00, 0x00, 0xFF) , # pixel 9
)
#----------------------------------------------------

# Create a buffer to record into
samples = array.array('H', [0] * SAMPLES)

# Setup the mic input
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK,
                       board.MICROPHONE_DATA,
                       sample_rate=SAMPLERATE,
                       bit_depth=16)

# Setup NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
max_dist = 0

while True:
    # Get raw mic data
    mic.record(samples, SAMPLES)

    # Clear DC Offset
    samples=sigproc.clearDCOffset(samples,SAMPLERATE)

    # Compute High/Low frequency ratio
    hlratio=sigproc.hlratio(samples,CUTOFF,SAMPLERATE)

    # Compute the distance from target ratio
    delta=abs(hlratio-RATIO_TARGET)
    max_dist=max(delta,max_dist)

    # Show on NeoPixels
    pixels.fill(0)
    pixel = round(simpleio.map_range(delta, 0, max_dist, 0, 9))
    pixels[pixel] = COLORS[pixel]
    pixels.show()

    time.sleep(DELAY)