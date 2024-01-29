from sonifiWaves import runSample
import asyncio
from rtlsdr import RtlSdr
from pynput import keyboard
import sys

_author_ = 'Faisal Umar, Lawrence Toomey'
_copyright_ = 'CSIRO, 2023'

cntr = 500
NFFT = 2 ** 7 + 1
dur = 3
singlePlay = False
sampleSize = 1000000

#init list/s of fixed frequency scrolling options for user
options = [
    
]
use_kbd = False
    
# initiate an sdr object
temp = RtlSdr()

# polling rate that is also band range?
temp.rs = 2**21
temp.rs_min = 1.024e6
temp.rs_max = temp.rs

# RTL-SDR dongle minimum and maximum frequency range (MHz)
temp.min_freq = 25.0 * 1e6
temp.max_freq = 1765.0 * 1e6

def on_press(key):
    return False
    

def scroll():
    return 1090

def isDigit(char):
    return char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' or char == '0'

def cleanInput(freq):
    idx = 0;
    
    while(not freq[idx] == '-' and not isDigit(freq[idx])):
        idx += 1

    return freq[idx:]

def intInput():
    #get integer input from the user, some needed variables
    freq = '500t'
    flag = False
    
    #let user know how to exit program
    print("Enter a negative number for frequency if you wish to exit program.")
    
    #re prompt user till input is a number
    while not freq.isdigit() and flag == False:
        #ask user for cntr freq they wanna explore
        freq = input("Enter a frequency in MHz you'd like to sonify: ")
        freq = cleanInput(freq)
        try:
            int(freq)
            flag = True
        except:
            flag = False
    
    return freq
                
def userInputs():
    
    while True:
        #init some needed vars for user input
        freq = "500t"
        
        #if user will use keys to scroll pre-selected frequencies
        if use_kbd:
            freq = scroll()
        else:
            freq = intInput()
        
        if(int(freq) <= 0):
            break
        
        #run the thing
        asyncio.run(runSample(int(freq), dur, NFFT, singlePlay, temp, sampleSize))
    
    #an explicite return statement for readability but isnt actually doing anything
    return

def appStart():
    #welcome user
    print("Welcome to the Sonification of Radio Waves Module for LoCUST.")
    
    #goto a function to get user inputs and run them while user still wants to
    userInputs()
    
    #thanks for using this module
    print("Thank you for using this Sonification of Radiowaves module!")

appStart()
