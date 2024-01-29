import numpy as np
from matplotlib.mlab import psd

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

def printInfo(a, f):
    #check valid result due to valid cntr value
    if(len(a) == 1 and len(f) == 1 and a[0] == 0 and f[0] == 0):
        print("Out of bounds value for frequency of the digitiser.")
        return a, f
    
    #output the current freq info
    for i in range(len(f)):
        print("Currently sonifying",round(f[i] / 1e6, 2),
              "MHz as", round(f[i] / 1e6, 2),
              "Hz audio, amplitude of",
              round(a[i], 2), 
              ".")
    
    #text file saving as needed
    file = open("audioLog.txt", "a")
    file.write("amplitudes: " + str(a) + ", frequencies: " + str(f) + "\n")
    file.close()

def radioWaves(cntr, NFFT=5, temp=5, low = 0.25, high = 1.0, sampleSize=1000):
    #check bound for frequency
    if(cntr * 1e6 < temp.min_freq or cntr * 1e6 > temp.max_freq):
        print("Out of bounds value for frequency from te RTL-SDR, please input",
              "between 25 MHz and 1765 MHz.")
        return [0], [0]
    
    # central freq to scan
    temp.fc = cntr * 1e6
    
    #get complex voltage sample
    ans = temp.read_samples(sampleSize)
    
    # remove the DC component
    ans = ans - np.mean(ans)
    
    # make some amount of FFTs off this data
    psd_scan_amps, f = psd(ans, NFFT=NFFT)
    
    #transform each value in both(?) arrays then return them
    f = (f * temp.rs / 2) + temp.fc
    
    #normalise the waves for amplitude in local window
    psd_scan_amps = psd_scan_amps ** (f[0] / 1e8)
    x5 = max(psd_scan_amps)
    x1 = min(psd_scan_amps)
    psd_scan_amps = ((high - low)/(x5 - x1)) * (psd_scan_amps - x1) + low
    
    #apply some more scaling and transformation to amplitudes
    psd_scan_amps = psd_scan_amps ** (3)
    
    #output diagnostic data
    printInfo(psd_scan_amps, f)

    #return the answer
    return psd_scan_amps, (f / 1e6)
