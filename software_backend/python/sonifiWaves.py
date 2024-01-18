from pyGameAudioOutput import sonifi, sonifi2, makeSounds, makePlot
import asyncio
import pygame
#from freqArrayMaker import radioWaves

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

#sonifi is freq in Hz, duration in milliseconds and amp 0-1 in float
#sonifi(200, 200, 0.5)
#sonifi(200, 200, 1.0)

async def runSample(cntr = 500, dur = 1, NFFT = 5, singlePlay = True, temp = 5, sampleSize = 1000):
    sampleRate = 44100

    pygame.mixer.init(sampleRate, -16, 2, 512)
    
    pygame.mixer.set_num_channels(NFFT)

    sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp, sampleSize))
    
    await asyncio.sleep(1)

    for i in range(10):
        if singlePlay:
            asyncio.ensure_future(sonifi(sounds.result(), cntr, dur))
        else:
            asyncio.ensure_future(sonifi2(sounds.result(), cntr, dur))
        #above does not do any outputs apart from audio

        sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp, sampleSize))

        print("Asynch start")
        await asyncio.sleep(dur * 1.1)
        print("Asynch loop restart")
    
    pygame.quit()
    
    return

#abstracted to user is cntr freq and duration of each tone played
#also level of NFFTs to be done in case
#runSample(cntr = 450, dur = 1)

#a few ideas are either terminal give a central freq or a pygame
#GUI (which defeats the purpose) to get inputs like central freq,
#ffts ie amount of wave band splitage, sound duration (each)
#and maybe a scaling function thats customisable from 0 to 1 volume by passing
#an extra pair param of start and end amplitudes to the freqArrayMaker function
