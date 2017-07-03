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
        data = wavfile.readframes(chunk) #reads the wav file and creates a variable with those values. although it will only go through 1024 or less frames  
        
    def generateMouthSignal(self,val):
        delta = val - self.prevAudiovalue 
        if( delta < -2 or val == 0 ):
            self.mouthValue = 0
        elif( delta > 0 ):
            self.mouthValue = 1

        self.prevAudiovalue = val
