from pyGameAudioOutput import sonifi, sonifi2
from freqArrayMaker import radioWaves

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

#sonifi is freq in Hz, duration in milliseconds and amp 0-1 in float
#sonifi(200, 200, 0.5)
#sonifi(200, 200, 1.0)

def runSample(cntr = 500, dur = 1, NFFT = 5, singlePlay = True, temp = 5):
    #radioWaves is center freq in MHz, NFFT as int of amt of bands
    a, f = [0.9, 0.4, 0.1, 0.8, 0.65], [1000, 200, 300, 500, 1100]
    #a, f = radioWaves(cntr, NFFT, temp)
    #above also has capability to modify lower and upper audio ranges as
    #low and high
    
    #check valid result due to valid cntr value
    if(len(a) == 1 and len(f) == 1 and a[0] == 0 and f[0] == 0):
        print("Out of bounds value for frequency of the digitiser.")
        return a, f 
    
    #print(a)
    #print(f / 1e6)
    
    for i in range(len(f)):
        #print(i)
        
        #output the current freq info
        print("Currently sonifying",round(f[i] / 1e6, 2),
              "MHz as", round(f[i] / 1e6, 2),
              "Hz audio, amplitude of",
              round(a[i], 2), 
              ".")
        
    #abstracted in fll form to freq in Hz to play, milliseconds of play
    #and amplitude in abs scale of [0, 1]
    if singlePlay:
        sonifi(f / 1e6, dur * 1000, a)
    else:
        sonifi2(f / 1e6, dur * 1000, a)
    #above does not do any outptus apart from audio
    
    return a, f;

#abstracted to user is cntr freq and duration of each tone played
#also level of NFFTs to be done in case
#runSample(cntr = 450, dur = 1)

#a few ideas are either terminal give a central freq or a pygame
#GUI (which defeats the purpose) to get inputs like central freq,
#ffts ie amount of wave band splitage, sound duration (each)
#and maybe a scaling function thats customisable from 0 to 1 volume by passing
#an extra pair param of start and end amplitudes to the freqArrayMaker function
