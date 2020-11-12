import RPi.GPIO as GPIO
import time

D = [10, 9, 11, 5, 6, 13, 19, 26]
L = [24, 25, 8, 7, 12, 16, 20, 21]

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
    for i in range (0, 8, 1):
        n = D[7-i]
        if b[i]==1:
            GPIO.output(n, 1)
        elif b[i]==0: 
            GPIO.output(n, 0)

def LEDS(number):
    b = int (number / 255 * 9)
    for i in range (0, 8, 1):
        n = L[i]
        if i < b:
            GPIO.output(n, 1)
        else:
            GPIO.output(n, 0)
            
def adc():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    x=0
    y=255
    while (y-x) > 1:
        p = int((x+y) / 2)
        num2dac(p)
        time.sleep(0.01)
        if GPIO.input(4) == 0:
            y = p
        else:
            x = p
    time.sleep(0.1)
    return p 

for i in range(0, 8, 1):
    GPIO.setmode(GPIO.BCM)
    n = D[i]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 0)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)
try:
    for k in range (0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = L[k]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    while True:
        V = adc()
        if V>0:
            print(round(V/255*3.2, 2), 'V',)
            lightNumber(V)
            LEDS(V)
            time.sleep(0.01)

except KeyboardInterrupt:
    print("You killed the function")
finally:
    for i in range(0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[i]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    GPIO.cleanup()
