import sys
import os
from rtlsdr import RtlSdr
import numpy as np
from matplotlib.mlab import psd

# print(os.path.abspath(rtlsdr.__file__))

# initiate an sdr object
temp = RtlSdr()

# polling rate that is also band range?
temp.rs = 2**21
temp.rs_min = 1.024e6
temp.rs_max = temp.rs

# central freq to scan
temp.fc = 1700 * 1e6

ans = temp.read_samples(2**21)

# raw data complex numbers
print(ans)

# remove the DC component
ans = ans - np.mean(ans)

#output wihtout DC component
print(ans)

# make some amount of FFTs off this data
psd_scan_amps, f = psd(ans, NFFT=5)

#output the strength of each FFT
print(psd_scan_amps)

#output freq of each as a normalised scale around the central fc band
print(f)

#output actual freq in MHz of first returned value
print(f[0] * (temp.rs / 2) + temp.fc)

#output the scan range of frequencies around this
print(2 * (temp.fc - (f[0] * (temp.rs / 2) + temp.fc)))

f = (f * temp.rs / 2) + temp.fc
print(f)

temp.close()

#better plan for future is async datacollection and make 1 fft from it
#then play that while async and queueing up the next wave sample

#for the asynch function have it play a split range into 3
#playing total of 3 seconds of audio