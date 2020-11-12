import RPi.GPIO as GPIO
import time
import array

GPIO.setmode(GPIO.BCM)

dac = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
GPIO.setup(4,GPIO.IN)
for i in dac:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

def decToBinList (decNumber):    
    a=bin(decNumber)
    b=a[2:11:1]
    c=b.zfill(8)
    d=[0, 0, 0, 0, 0, 0, 0, 0,]
    for i in range(8):
        d[i]=int(c[i])
    return (d)

def dec(value):
    k = decToBinList(value)
    for i in range(8):
        if k[i]==1:
            GPIO.output((dac[i]),1)
        else: GPIO.output((dac[i]),0)
try:
    while True:
        p = 1
        for value in range(256):
            dec(value)
            time.sleep(0.01)
            if GPIO.input(4)==0:
                print(value)
                voltage = value*3.3/255
                p = 0 
                print(voltage)
                break
        if p==1:
            break       
        
                
except KeyboardInterrupt: 
    for i in range(len(dac)):
        GPIO.output((dac[i]),0)

finally:
    for i in range(len(dac)):
        GPIO.output((dac[i]),0)

GPIO.cleanup()


