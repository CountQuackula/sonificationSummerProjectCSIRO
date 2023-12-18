import numpy
import pygame
from timeit import default_timer as timer

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

def sonifi(frequency, dur, amp):
    #sample rate and others are al just values
    #the 2 in thingy is stereo sound 1 would be mono
    #freq is in Hz and dur in miliseconds which is the precision
    #i wanted anyway so thats cool
    #freq is between human auditory range, dur is in milisecond int and amp
    #is 0 to 1 inclusive floating
    sampleRate = 44100
    
    pygame.mixer.init(sampleRate, -16, 2, 512)
    
    for i in range(len(frequency)):
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * frequency[i] * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        arr2 = numpy.c_[arr, arr]
        sound = pygame.sndarray.make_sound(arr2)
        sound.play(-1)
        sound.set_volume(amp[i])
        pygame.time.delay(dur)
        sound.stop()

def sonifi2(frequency, dur, amp):
    #print("Hello World!")
    
    start = timer()
    
    sampleRate = 4410
    
    pygame.mixer.init(sampleRate, -16, 2, 512)
    pygame.mixer.set_num_channels(len(amp))
    
    sounds = []
    
    for i in range(len(frequency)):
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * frequency[i] * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        arr2 = numpy.c_[arr, arr]
        sound = pygame.sndarray.make_sound(arr2)
        sound.set_volume(amp[i])
        sounds.append(sound)
    
    print(timer() - start)
        
    for s in sounds:
        pygame.mixer.find_channel().play(s, dur)
    
    pygame.time.delay(dur)
    
    pygame.quit()