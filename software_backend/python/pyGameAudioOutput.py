import numpy
import pygame
from timeit import default_timer as timer
from freqArrayMaker import radioWaves, printInfo
import matplotlib.pyplot as plt
import asyncio

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

#an incompleted function that is supposed to create a live plot of the data
#but at present causes the program to freeze and hasnt been resolved
async def makePlot(a, f):
    plt.hist(x=f, bins=len(f), weights=a, color='skyblue', edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Freq')
    plt.title('Test Basic Hist')
    plt.pause(0.1)
    plt.show()
    print("Hist made?")
    

async def makeSounds(cntr, NFFT, temp, sampleSize = 1000):
    print("Producing Sounds")
    #start = timer()

    #radioWaves is center freq in MHz, NFFT as int of amt of bands
    amp, frequency = radioWaves(cntr, NFFT, temp, sampleSize=sampleSize)
    #above also has capability to modify lower and upper audio ranges as
    #low and high

    sampleRate = 44100
    
    sound = []
    
    for i in range(len(frequency)):
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * frequency[i] * x / sampleRate) for x in range(0, round(sampleRate / frequency[i]))]).astype(numpy.int16)
        arr2 = numpy.c_[arr, arr]
        s = pygame.sndarray.make_sound(arr2)
        s.set_volume(amp[i])
        sound.append(s)

    #print(str(timer() - start) + " is make sounds time.")

    print("Sounds Produced")
    return sound

async def sonifi(sounds, f, dur):
    start = timer()
    
    #individual audio playback of the generated audio tones
    for i in range(len(sounds)):
        pygame.mixer.Channel(0).play(sounds[i], round(f * dur) + f)
        await asyncio.sleep(dur / len(sounds))
    
    print("Sounds singular playing took: " + str(timer() - start))

async def sonifi2(sounds, f, dur):
    start = timer()
    
    #synthesis of the generated audio tones
    for i in range(len(sounds)):
        pygame.mixer.Channel(i).play(sounds[i], round(f * dur) + f)

    #start = timer()
    print("Loading sounds took: " + str(timer() - start))
    await asyncio.sleep(dur)
    #print("Awoke after sleep " + str(timer() - start))