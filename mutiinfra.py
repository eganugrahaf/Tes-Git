import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings (False)
GPIO.setup(10,GPIO.IN)
GPIO.setwarnings (False)
while True:
    if GPIO. input(10)==0:
        print("menyala")
        time.sleep(0.1)
    else:
        print("u")
        time.sleep(0.1)
