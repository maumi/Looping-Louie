import RPi.GPIO as GPIO
import time
import smbus
from threading import Thread
from multiprocessing import Process

GPIO.setmode(GPIO.BOARD)

taster = 40
GPIO.setup(taster, GPIO.IN)

i = 0

b = smbus.SMBus(1)
address = 0x20 # I2C Adresse
b.write_byte_data(0x20,0x00,0x00)
b.write_byte_data(0x20,0x01,0x00)

hexe = 0x04

print hexe
b.write_byte_data(0x20,0x14,0x04)
b.write_byte_data(0x20,0x14,hexe+0x02)
print hexe

def test():
	global i
	while True:
		if not (GPIO.input(taster)):
			i = i+1
			print "bla", i
		time.sleep(0.01)
		

t = Process(target=test, args=())
t.daemon = True
t.start()

time.sleep(5)
t.terminate()
t.join()

GPIO.cleanup()
