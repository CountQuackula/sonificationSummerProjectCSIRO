from sonifiWaves import runSample
import asyncio
#from rtlsdr import RtlSdr

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

cntr = 500
dur = 5
NFFT = 5
singlePlay = False
    
# initiate an sdr object
temp = 5

# polling rate that is also band range?
#temp.rs = 2**21
#temp.rs_min = 1.024e6
#temp.rs_max = temp.rs

# RTL-SDR dongle minimum and maximum frequency range (MHz)
#temp.min_freq = 25.0 * 1e6
#temp.max_freq = 1765.0 * 1e6

def userInputs():
    
    while True:
        #let user know thy can exit program by entering negative number for either field
        print("If you wish to exit the program please enter a negative"+
              "number into (any) field/s below")
        
        flag = False
        freq = "500t"
        
        #re prompt user till input is a number
        while not freq.isdigit() and flag == False:
            #ask user for cntr freq they wanna explore
            freq = input("Enter a frequency in MHz you'd like to sonify: ")
            try:
                int(freq)
                flag = True
            except:
                flag = False
        
        flag = False
        
        if(int(freq) <= 0):
            break
        
        #run the thing
        #loop = asyncio.get_event_loop()
        asyncio.run(runSample(int(freq), dur, NFFT, singlePlay, temp))
    
    #an explicite return statement for readability but isnt actually doing anything
    return

def appStart():
    #welcome user
    print("Welcome to the Sonification of Radio Waves Module for LoCUST.")
    
    print("By default the central frequency we will scan around starts at 500"+
          "MHz with a duration of 1 second. The following is an example.")
    
    #a, f = runSample(cntr, dur, NFFT, singlePlay, temp);
    
    #goto a function to get user inputs and run them while user still wants to
    userInputs()
    
    #thanks for using this module
    print("Thank you for using this Sonification of Radiowaves module!")

appStart()

#temp.close()