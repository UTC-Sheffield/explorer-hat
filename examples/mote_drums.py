#------------------------------------------------------------------------------#
#--------------------Beautifully programmed by Josh Hall-----------------------#
#------------------------------------------------------------------------------#

#!/usr/bin/env python
from mote import Mote # Imports library 'Mote' for LED's
import time # Imports library 'Time'

################################################################################

# Sets channels for different LED's

mote=Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

################################################################################

# Importing libraries 'Signal' 'Exit' 'pygame' and 'explorerhat'

import signal
from sys import exit

try:
    import pygame
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

import explorerhat

################################################################################

# Prints text to screen describing what the program does

print("""
Turns your Explorer HAT and Mote into a drum kit with light show!

Hit any touch pad to hear a drum sound.

Press CTRL+C to exit.
""")

################################################################################

# Clears LED's

mote.clear()

################################################################################

# Audio for each note

samples = [                         
    'sounds/hit.wav',
    'sounds/ting.wav',
    'sounds/clap.wav',
    'sounds/smash.wav',
    'sounds/hat.wav',
    'sounds/crash.wav',
    'sounds/rim.wav',
    'sounds/thud.wav'
]

################################################################################

# Setting up sound system
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

################################################################################

# Sets up an array for the sound effects
sounds = []
for x in range(8):
    sounds.append(pygame.mixer.Sound(samples[x]))

offset = 0                  # A counter to add variety to the LED colours


# When something is touched this function is called with the button channel (ch) and the event name
def handle(ch, evt):

    global offset           # Allows use of variable offset in functions
    if ch > 4:              # Changes from 8 button channels to 4 light channels
        channel = ch - 4        
    else:
        channel = ch
        
    if evt == 'press':      # If the event is a press event
        sounds[ch - 1].play(loops=0) # Plays sounds once
        name = samples[ch - 1].replace('sounds/','').replace('.wav','')
        # Finds out name of sound and removes .wav 
        print("{}!".format(name.capitalize())) # Adds '!' to the end of sound
        
        # Sets LED colours when pressed
        for pixel in range(16):
            mote.set_pixel(channel,pixel,
                           (37*(offset+9))%255,
                           (73*(offset+3))%255,
                           (51*(offset+7))%255)
            
        
        mote.show()
        offset = offset+1

################################################################################




explorerhat.touch.pressed(handle)
explorerhat.touch.released(handle)


signal.pause()
# Stops python from closing straight away and pauses waiting for the buttons to be pressed






#------------------------------------------------------------------------------#
#--------------------Beautifully commented by Louis Putland--------------------#
#------------------------------------------------------------------------------#
