import numpy
import pygame
from timeit import default_timer as timer
from freqArrayMaker import radioWaves, printInfo
import asyncio

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

async def makeSounds(cntr, NFFT, temp):
    start = timer()

    #radioWaves is center freq in MHz, NFFT as int of amt of bands
    amp, frequency = radioWaves(cntr, NFFT, temp)
    #above also has capability to modify lower and upper audio ranges as
    #low and high

    sampleRate = 44100
    
    pygame.mixer.init(sampleRate, -16, 2, 512)
    
    sound = []
    
    for i in range(len(frequency)):
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * frequency[i] * x / sampleRate) for x in range(0, round(sampleRate / frequency[i]))]).astype(numpy.int16)
        arr2 = numpy.c_[arr, arr]
        s = pygame.sndarray.make_sound(arr2)
        s.set_volume(amp[i])
        sound.append(s)

    print(str(timer() - start) + " is make sounds time.")

    return sound

async def sonifi(frequency, dur, amp):
    #sample rate and others are al just values
    #the 2 in thingy is stereo sound 1 would be mono
    #freq is in Hz and dur in miliseconds which is the precision
    #i wanted anyway so thats cool
    #freq is between human auditory range, dur is in milisecond int and amp
    #is 0 to 1 inclusive floating
    sampleRate = 44100
    
    pygame.mixer.init(sampleRate, -16, 2, 512)
    
    #update thios function to be asynch in the sense that it sonofies 1 freq and plays it immedietly and waits
    #to play the next one but has it generated
    for i in range(len(frequency)):
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * frequency[i] * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        arr2 = numpy.c_[arr, arr]
        sound = pygame.sndarray.make_sound(arr2)
        sound.play(-1)
        sound.set_volume(amp[i])
        pygame.time.delay(dur)
        sound.stop()

async def sonifi2(sounds, f, dur):
    start = timer()

    sampleRate = 44100
    
    pygame.mixer.init(sampleRate, -16, 2, 512)

    for s in sounds:
        pygame.mixer.find_channel().play(s, round(f * dur))
    
    print("Everything started returning control for an asyncio sleep")
    await asyncio.sleep(dur)
    print("Awoke after sleep " + str(timer() - start))

    pygame.quit()