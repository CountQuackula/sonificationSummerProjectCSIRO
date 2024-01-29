from pyGameAudioOutput import sonifi, sonifi2, makeSounds
import asyncio
import pygame
from pynput import keyboard
import time
#from freqArrayMaker import radioWaves

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

break_program = False
def on_press(key):
    global break_program
    if key.char == 'q':
        print(', exit key pressed')
        break_program = True
        return False

async def runSample(cntr = 500, dur = 1, NFFT = 5, singlePlay = True, temp = 5, sampleSize = 1000):
    with keyboard.Listener(on_press=on_press) as listener:
        
        sampleRate = 44100
    
        pygame.mixer.init(sampleRate, -16, 2, 512)
        
        pygame.mixer.set_num_channels(NFFT)
    
        sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp, sampleSize))
        
        await asyncio.sleep(1)
        
        print("Starting audio, press q to quit loop and return to frequency menu.")
    
        while break_program == False:
            if singlePlay:
                asyncio.ensure_future(sonifi(sounds.result(), cntr, dur))
            else:
                asyncio.ensure_future(sonifi2(sounds.result(), cntr, dur))
            #above does not do any outputs apart from audio
    
            sounds = asyncio.ensure_future(makeSounds(cntr, NFFT, temp, sampleSize))
    
            print("Asynch start")
            await asyncio.sleep(dur * 1.1)
            print("Asynch loop restart")
        listener.join()
    
    pygame.quit()
    
    return
