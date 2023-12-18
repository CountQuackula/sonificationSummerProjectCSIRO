import sys
import os
import numpy as np
from matplotlib.mlab import psd
#from timeit import default_timer as timer

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

def radioWaves(cntr, NFFT=5, temp=5, low = 0.25, high = 1.0):
    # print(os.path.abspath(rtlsdr.__file__))
    
    if(cntr * 1e6 < temp.min_freq or cntr * 1e6 > temp.max_freq):
        print("Out of bounds value for frequency from te RTL-SDR, please input between",
              "25 MHz and 1765 MHz.")
        return [0], [0]
    # central freq to scan
    temp.fc = cntr * 1e6
    
    #start = timer()
    ans = temp.read_samples(1000)
    #print(timer() - start)
    
    # raw data complex numbers
    #print(ans)
    
    # remove the DC component
    ans = ans - np.mean(ans)
    
    #output wihtout DC component
    #print(ans)
    
    # make some amount of FFTs off this data
    #start = timer()
    psd_scan_amps, f = psd(ans, NFFT=NFFT)
    #print(timer() - start)
    #output the strength of each FFT
    #print(psd_scan_amps)
    
    #output freq of each as a normalised scale around the central fc band
    #print(f)
    
    #output actual freq in MHz of first returned value
    #print(f[0] * (temp.rs / 2) + temp.fc)
    
    #output the scan range of frequencies around this
    #print(2 * (temp.fc - (f[0] * (temp.rs / 2) + temp.fc)))
    
    #transform each value in both(?) arrays then return them
    f = (f * temp.rs / 2) + temp.fc
    
    #normalise the waves for amplitude in local window
    x5 = max(psd_scan_amps)
    x1 = min(psd_scan_amps)
    #print(psd_scan_amps)
    #print(x5)
    #print(x1)
    psd_scan_amps = ((high - low)/(x5 - x1)) * (psd_scan_amps - x1) + low
    
    return psd_scan_amps, f
    
    #better plan for future is async datacollection and make 1 fft from it
    #then play that while async and queueing up the next wave sample
    
    #for the asynch function have it play a split range into 3
    #playing total of 3 seconds of audio