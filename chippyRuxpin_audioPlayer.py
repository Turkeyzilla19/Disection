#!/usr/bin/env python
#
# Chippy Ruxpin by Next Thing Co 2015
# Powered by C.H.I.P., the world's first $9 computer!

#!/usr/bin/env python
#

from time import sleep
import math
import array
import wave
import os
import subprocess

class AudioPlayer:
    def __init__(self):
        self.prevAudiovalue = 0
        self.mouthValue = 0
        
    def play(self,fileName):
        # Initialise matrix
        matrix=[0,0,0,0,0,0,0,0] #makes a matrix

        # Set up audio
        wavfile = wave.open(fileName,'r') #opens the wav file and sets it to read mode
        chunk = 1024 #creates a variable with a value of 1024
        data = wavfile.readframes(chunk) #reads the wav file and creates a variable with those values. although it will  
        try:
          while data!='':
             output.write(data)
             # Split channel data and find maximum volume   
             channel_l=audioop.tomono(data, 2, 1.0, 0.0)
             channel_r=audioop.tomono(data, 2, 0.0, 1.0)
             max_vol_factor =5000
             max_l = audioop.max(channel_l,2)/max_vol_factor
             max_r = audioop.max(channel_r,2)/max_vol_factor

             for i in range (1,8):
                self.generateMouthSignal((1<<max_r)-1)
                
             data = wavfile.readframes(chunk)
        except:
          data = None
        
        os.system( '/etc/init.d/alsa-utils restart' )
        sleep( .25 )

    def generateMouthSignal(self,val):
        delta = val - self.prevAudiovalue 
        if( delta < -2 or val == 0 ):
            self.mouthValue = 0
        elif( delta > 0 ):
            self.mouthValue = 1

        self.prevAudiovalue = val
