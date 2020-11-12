import RPi.GPIO as GPIO
import time

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

def adc():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    f = 0
    b = 0
    for i in range (0, 255, 1):
        a = int(GPIO.input(4))
        if a == 0:
            b = 1
            f = i
            break
    if b == 1 and f > 0:
        num2dac(f)
        time.sleep(0.1)
        V = float(f)/255*3.2
        return V
    else:
        return 0



for i in range(0, 8, 1):
    GPIO.setmode(GPIO.BCM)
    n = D[i]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 0)

for i in range(0, 8, 1):
    GPIO.setmode(GPIO.BCM)
    n = D[i]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 0)
    break


try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    for i in range (0, 255, 1):
        a = int(GPIO.input(4))
        print(a)

except KeyboardInterrupt:
    print("You killed the function")
finally:
    for i in range(0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[i]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
    GPIO.cleanup()