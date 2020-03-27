#!/usr/bin/env python

##################################################################
#
# Simple simulation on of Sine function
#

import matplotlib.pyplot as plt
import numpy as np


# TODO: remove these line for the assignment

# Module for generating binary sequence from binary data
def binary_seq(data,symlen):
    # data      : binary data
    # symlen    : symbol duration (number of samples in one symbol)
    import numpy as np
    sig = np.repeat(data, symlen)
    return sig

#
# Define parameters
#
Fs = 1000       # Sampling frequency for the signal: number of samples per second
Pi = np.pi      # Pi - uses numpy.pi constant
f = 50          # Frequency of sine function (carrier frequency in Hertz)
A = 1           # Amplitude of the sine function
datarate = 8    # in bit/second

#
# Binary message
#
binary_msg = np.array([1,0,1,1,1,0,0,1])    # original binary message
symbol_len = int(Fs/datarate)               # number of samples per symbol
msg = binary_seq(binary_msg, symbol_len)    # create binary sequence

# time vector
t_end = Fs * len(binary_msg)/datarate       # length of time sequence
t = np.arange(0, t_end/Fs, 1/Fs)            # time vector

# Sine function - carrier
y = np.sin(2*Pi*f*t)

# Analog message function
fm = 2          # Frequency of analog function (in Hertz)
msg2 = np.sin(2*Pi*fm*t)

#
# DEBUG
# TODO: remove these line for the assignment
#
print("Value of T_End = %d" %(t_end))
print("Length of time vector = %4d" % (len(t)))
print("Length of msg  vector = %4d" % (len(msg)))
print("Length of sine vector = %4d" % (len(y)))


# Modulated signal

# TODO: remove these line for the assignment
M1 = msg * y
M2 = msg2 * y

#
# INSTRUCTION for the STUDENT:
# implement your own code for the modulated signal here
#


##################################################################
#
# Plotting data
#

# Binary data sequence
plt.figure(1)
plt.plot(t,msg)
# Give title for plot
plt.title('Binary message')
# Give x axis label for the sine wave plot
plt.xlabel('Time')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both')

# Save figure to file
foldername = 'sim/'
basename = 'simplot_'
modelname = 'binary'
filetype = '.png'
filename = foldername + basename + modelname + filetype
plt.savefig(filename, bbox_inches='tight')

# Carrier signal
plt.figure(2)
# Plot the sine wave using time and amplitude obtained for the sine wave
plt.plot(t, y)
# Give a title for the sine wave plot
plt.title('Carrier wave - Sine function')
# Give x axis label for the sine wave plot
plt.xlabel('Time')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Save figure to file
modelname = 'carrier'
filename = foldername + basename + modelname + filetype
plt.savefig(filename, bbox_inches='tight')


# Modulated signal
plt.figure(3)
plt.plot(t,M1)
# Give a title for the sine wave plot
plt.title('Binary modulated signal')
# Give x axis label for the sine wave plot
plt.xlabel('Time')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Save figure to file
modelname = 'modbin'
filename = foldername + basename + modelname + filetype
plt.savefig(filename, bbox_inches='tight')

# Analog message function
plt.figure(4)
plt.plot(t,msg2)
# Give a title for the sine wave plot
plt.title('Analog message wave')
# Give x axis label for the sine wave plot
plt.xlabel('Time')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Save figure to file
modelname = 'analog'
filename = foldername + basename + modelname + filetype
plt.savefig(filename, bbox_inches='tight')


# Modulated signal form Analog message function
plt.figure(5)
plt.plot(t,M2)
# Give a title for the sine wave plot
plt.title('Modulated signal from analog message')
# Give x axis label for the sine wave plot
plt.xlabel('Time')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Save figure to file
modelname = 'modanalog'
filename = foldername + basename + modelname + filetype
plt.savefig(filename, bbox_inches='tight')

# Show figure on the terminal
plt.show()
