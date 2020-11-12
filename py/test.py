import RPi.GPIO as GPIO
import time 

D = [24, 25, 8, 7, 12, 16, 20, 21]

def lightUP(ledNumber, period):
    GPIO.setmode(GPIO.BCM)
    n = D[ledNumber]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 1)
    time.sleep(period)
    GPIO.output(n, 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    GPIO.setmode(GPIO.BCM)
    n = D[ledNumber]
    GPIO.setup(n, GPIO.OUT)
    for i in range(0, blinkCount, 1):
        GPIO.output(n, 1)
        time.sleep(blinkPeriod)
        GPIO.output(n, 0)
        time.sleep(blinkPeriod)

def runLight(count, period):
    GPIO.setmode(GPIO.BCM)
    for i in range (0, count, 1):
        for k in range (0, 8, 1):
            n = D[k]
            GPIO.setup(n, GPIO.OUT)
            GPIO.output(n, 1)
            time.sleep(period)
            GPIO.output(n, 0)

def runDark(count, period):
    GPIO.setmode(GPIO.BCM)
    for k in range (0, 8, 1):
        n = D[k]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 1)
    for i in range (0, count, 1):
        for k in range (0, 8, 1):
            n = D[k]
            GPIO.setup(n, GPIO.OUT)
            GPIO.output(n, 0)
            time.sleep(period)
            GPIO.output(n, 1)
    for k in range (0, 8, 1):
        n = D[k]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)

def decToBin(decNumber):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    k = 7
    while decNumber > 0:
        b[k] = int(decNumber % 2)
        decNumber = decNumber // 2
        k -= 1 
    return b     

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

def runPattern(pattern, direct):
    if direct > 0:
        while direct >= 0:
            for i in range(0, direct+1, 1):
                lightNumber(pattern << i)
                time.sleep(1)
                direct -= 1
                for k in range (0, 8, 1):
                    GPIO.setmode(GPIO.BCM)
                    n = D[k]
                    GPIO.setup(n, GPIO.OUT)
                    GPIO.output(n, 0)
                    
    else:
        while direct <= 0:
            for i in range(0, -direct+1, 1):
                lightNumber(pattern << 8-i)
                time.sleep(1)
                direct += 1 
                for k in range (0, 8, 1):
                    GPIO.setmode(GPIO.BCM)
                    n = D[k]
                    GPIO.setup(n, GPIO.OUT)
                    GPIO.output(n, 0)

def PWM1(number, fr):
    GPIO.setmode(GPIO.BCM)
    n = D[number]
    GPIO.setup(n, GPIO.OUT)

    p = GPIO.PWM(n, fr)
    p.start(0)
    try:
        while True:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.2)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.2)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()

for k in range (0, 8, 1):
        GPIO.setmode(GPIO.BCM)
        n = D[k]
        GPIO.setup(n, GPIO.OUT)
        GPIO.output(n, 0)
while True:
    #n = input()
    #if n==1:

    c = input()
    p = input()
    #runDark(c, p)
    PWM1(c, p)