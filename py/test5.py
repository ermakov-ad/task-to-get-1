import RPi.GPIO as GPIO
import time
import numpy as np
from time import sleep
import math 
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io




D = [10, 9, 11, 5, 6, 13, 19, 26]

def decToBin(decNumber):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    k = 7
    while decNumber > 0:
        b[k] = int(decNumber % 2)
        decNumber = decNumber // 2
        k -= 1 
    return b

def num2dac(value):
    value = lightNumber(value)

def lightNumber(number):
    b = decToBin(number)
    for k in range (0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[k]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    for i in range (0, 8, 1):
        if b[i]==1:
            GPIO.setmode(GPIO.BCM)
            n = D[7-i]
            GPIO.setup(n, GPIO.OUT)
            GPIO.output(n, 1)

for i in range(0, 8, 1):
    GPIO.setmode(GPIO.BCM)
    n = D[i]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 0)

try:
    samplerate, data = wavfile.read('/home/gr006/Desktop/Scripts/Panasik_Ermakov/SOUND.WAV')
    amplitude = data[:, 0]
    sf = 1/44000
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

    # for i in amplitude:
    #     num2dac(int(i))
    #     time.sleep(sf)
except KeyboardInterrupt:
    print("You killed the function")
finally:
    for i in range(0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[i]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    GPIO.cleanup()