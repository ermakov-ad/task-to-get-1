import RPi.GPIO as GPIO
import time 

D = [24, 25, 8, 7, 12, 16, 20, 21]

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

def num2dac (value):
    p=0
    for j in range(0,2**bit_depth):
        N=[0,0,0,0,0,0,0,0]
        value = j
        print(value)
        p = int(value/256)
        q = value%256
        N = decToBin(q + p)
        for i in range(0, bit_depth):
            GPIO.output(D[i], N[i])
        time.sleep(0.3)

for k in range (0, 8, 1):
    GPIO.setmode(GPIO.BCM)
    n = D[k]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 0)
while True:
    print("Введите номер функции:")
    n = input()
    if (n==(-1)):
        break
    elif (n==1):
        while True:
            print("Введите число:")
            value = int(input())
            if (value>=0 and value<=255):
                num2dac(value)
            elif (value==(-1)):
                break
            else:
                print("Некорректный ввод")