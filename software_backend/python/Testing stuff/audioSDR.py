import pyaudio
import math

def playTone(freq, length):
    bit_rate = 16000 #the number of frames per second
    
    frequency = freq #in herts
    play_time = length #in second to play sound
    
    if frequency > bit_rate:
        bit_rate = frequency + 100
    
    num_frames = int(bit_rate * play_time)
    total_frames = num_frames % bit_rate
    wave_info = ''
    
    for x in range(total_frames):
        wave_info = wave_info+chr(128)
    
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(1),
                    channels = 1,
                    rate = bit_rate,
                    output = True)
    
    stream.write(wave_info)
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    frequency = 500 #Hz
    duration = 2 #in seconds
    
    #Pyaudio = pyaudio.Pyaudio
    
    #funcation to play frequency for given duration
    playTone(frequency, duration)