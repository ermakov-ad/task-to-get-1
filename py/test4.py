import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import math 

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
#    while True:
    f = 440*8
    sf = 1/44000
    t = np.arange(0, 1, sf)
    amplitude = 255 * (np.sin(2*math.pi*f*t) + 1) // 2
 #   plt.plot(t, amplitude)
    # plt.title('Синус')
    # plt.xlabel('Время')
    # plt.ylabel('Амплитуда sin(time)')
    # plt.show()

    for i in range(0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[i]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)

    for i in amplitude:
        num2dac(int(i))
        time.sleep(sf)

except KeyboardInterrupt:
    print("You killed the function")
finally:
    for i in range(0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[i]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    GPIO.cleanup()