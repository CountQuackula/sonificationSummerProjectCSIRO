from pyGameAudioOutput import sonifi, sonifi2, makeSounds
import asyncio
#from freqArrayMaker import radioWaves

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

#sonifi is freq in Hz, duration in milliseconds and amp 0-1 in float
#sonifi(200, 200, 0.5)
#sonifi(200, 200, 1.0)

async def runSample(cntr = 500, dur = 1, NFFT = 5, singlePlay = True, temp = 5):
    sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp))

    await asyncio.sleep(1)
    print("First audio generated")

    for i in range(2):
        if singlePlay:
            sonifi(sounds, cntr, dur)
        else:
            asyncio.ensure_future(sonifi2(sounds, cntr, dur))
        #above does not do any outptus apart from audio

        sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp))
            
        print("actions 1")
        await asyncio.sleep(5.01)
        print("loop restart")
    
    return

#abstracted to user is cntr freq and duration of each tone played
#also level of NFFTs to be done in case
#runSample(cntr = 450, dur = 1)

#a few ideas are either terminal give a central freq or a pygame
#GUI (which defeats the purpose) to get inputs like central freq,
#ffts ie amount of wave band splitage, sound duration (each)
#and maybe a scaling function thats customisable from 0 to 1 volume by passing
#an extra pair param of start and end amplitudes to the freqArrayMaker function
