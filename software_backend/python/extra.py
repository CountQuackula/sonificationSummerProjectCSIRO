import pygame
import numpy
import time

sampleRate = 44100
    
pygame.mixer.init(sampleRate, -16, 2, 512)

f = 1250

arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * f * x / sampleRate) for x in range(0, round(sampleRate / f))]).astype(numpy.int16)
arr2 = numpy.c_[arr, arr]
s = pygame.sndarray.make_sound(arr2)
s.set_volume(0.5)

pygame.mixer.find_channel().play(s, round(f * 5))

time.sleep(1)

print("Just paused for 5 seconds?")

pygame.quit()