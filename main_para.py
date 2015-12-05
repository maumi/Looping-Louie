import RPi.GPIO as GPIO
import smbus
from time import sleep
from random import randrange,randint
from threading import Thread,Lock
from multiprocessing import Process

#global speed
speed = 20
#global clockwise
clockwise = 1
lock = Lock()
button_active = False
boost_active = False
game_running = False

#global hex led
hexe = 0x00

smbus = smbus.SMBus(1)

#vor 
Motor1A = 16
#zurueck
Motor1B = 18
#an
Motor1E = 22

#LEDS
#start GPB0 0x01
#B1 GPA4 0x10
#B2 GPA5 0x20
#B3 GPA6 0x40
#B4 GPA7 0x80
#B5 GPA0 0x01
#B6 GPA2 0x04
#B7 GPA1 0x02
#B8 GPA3 0x08

#Taster
Bs = 32
B1 = 35
B2 = 33
B3 = 31
B4 = 29
B5 = 36
B6 = 40
B7 = 38
B8 = 37 

GPIO.setmode(GPIO.BOARD)

#alles ausgaenge 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

# we set the PWM controller to Motor1A for forward movement with 250 Hz frequency
pwm1A = GPIO.PWM( Motor1A, 250 ) 
# we do the same for Motor1B (for reverse movement)
pwm1B = GPIO.PWM( Motor1B,250 )

# we start both pwm controllers to zero duty cycle( off )
pwm1A.start( 0 )
pwm1B.start( 0 )

def button_init():
	#GPIO.setmode(GPIO.BOARD)
	global smbus

	# Die 9 LEDs raussuchen und ausschalten
	#GPIO.setup(B1, GPIO.OUT)
	#GPIO.output(B1, False)
	smbus.write_byte_data(0x20,0x00,0x00) # Bank A Ausgang
	smbus.write_byte_data(0x20,0x01,0x00) # Bank B Ausgang
	smbus.write_byte_data(0x20,0x14,0x00) # Bank A alle aus
	smbus.write_byte_data(0x20,0x15,0x00) # Bank B alle aus
	
	# Die 9 Buttons als Eingaenge
	GPIO.setup(Bs, GPIO.IN)
	GPIO.setup(B1, GPIO.IN)
	GPIO.setup(B2, GPIO.IN)
	GPIO.setup(B3, GPIO.IN)
	GPIO.setup(B4, GPIO.IN)
	GPIO.setup(B5, GPIO.IN)
	GPIO.setup(B6, GPIO.IN)
	GPIO.setup(B7, GPIO.IN)
	GPIO.setup(B8, GPIO.IN)
		
def boost_wait_b0():
	global smbus,hexe,game_running
	while True:
		#sleep(5)
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x10
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		print "b1 ready"
		# Button Boost Thread aktivieren
		t = Process(target=pressed_b0, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
		
def boost_wait_b1():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x20
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b1, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
		
def boost_wait_b2():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x40
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b2, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)

		
def boost_wait_b3():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x80
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b3, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
		
def boost_wait_b4():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x01
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b4, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
		
def boost_wait_b5():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		#sleep(5)
		print "b6 ready"
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x04
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b5, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
		
def boost_wait_b6():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x02
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b6, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
			
def boost_wait_b7():
	global hexe,smbus,game_running
	while True:
		sleep(randint(20,50))
		# LED von Taster 0 aktivieren
		lock.acquire()
		hexe = hexe+0x08
		smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
		lock.release()
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b7, args=())
		#t.daemon = True
		t.start()
		t.join()
		sleep(.01)
	
def pressed_b0():
	global boost_active,smbus,B1,hexe,game_running
	while True:
		if not game_running:
			return
		if not (GPIO.input(B1)):			
			boost_active = True	
			print "b1 pressed"
			lock.acquire()
			hexe = hexe - 0x10
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x10) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x10) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x10) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b1():
	global boost_active,smbus,B2,hexe,game_running
	while True:
		if not game_running:
			return
		if not (GPIO.input(B2)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x20
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x20) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x20) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x20) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b2():
	global boost_active,smbus,B3,hexe,game_running
	while True:
		if not game_running:
			return
		if not (GPIO.input(B3)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x40
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x40) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x40) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x40) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b3():
	global boost_active,smbus,B4,hexe,game_running
	#button_init()
	#button_gpio = 11
	while True:
		if not game_running:
			return
		if not (GPIO.input(B4)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x80
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x80) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x80) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x80) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b4():
	global boost_active,smbus,B5,hexe,game_running
	#button_init()
	#button_gpio = 11
	while True:
		if not game_running:
			return
		if not (GPIO.input(B5)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x01
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x01) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x01) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x01) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b5():
	global boost_active,smbus,B6,hexe,game_running
	#button_init()
	#button_gpio = 11
	while True:
		if not game_running:
			return
		if not (GPIO.input(B6)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x04
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			print "bling"
			smbus.write_byte_data(0x20,0x14,hexe+0x04) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			print "bling"
			smbus.write_byte_data(0x20,0x14,hexe+0x04) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			print "bling"
			smbus.write_byte_data(0x20,0x14,hexe+0x04) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b6():
	global boost_active,smbus,B7,hexe,game_running
	while True:
		if not game_running:
			return
		if not (GPIO.input(B7)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x02
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x02) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x02) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x02) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_b7():
	global boost_active,smbus,B8,hexe,game_running
	#button_init()
	#button_gpio = 11
	while True:
		if not game_running:
			return
		if not (GPIO.input(B8)):			
			boost_active = True	
			lock.acquire()
			hexe = hexe - 0x08
			lock.release()
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			#3x aufblinken
			smbus.write_byte_data(0x20,0x14,hexe+0x08) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x08) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe+0x08) # Bank B alle aus
			sleep(.3)
			smbus.write_byte_data(0x20,0x14,hexe) # Bank B alle aus
			sleep(2)
			return
		sleep(0.01)
        
def pressed_bstart():
	global game_running,Bs,smbus,hexe
	button_init()
	#print "bstart"
	GPIO.setup(Bs, GPIO.IN)
	#button_gpio = 11
	while True:
		if not (GPIO.input(Bs)):	
			if game_running:	
				#Spiel stoppen
				print "stop game"
				lock.acquire()
				smbus.write_byte_data(0x20,0x15,0x00) # Start LED aus
				hexe = 0x00
				lock.release()
				game_running = False
				sleep(2)
				return
			elif not game_running:
				#Spiel Starten
				print "start game"
				lock.acquire()
				#hexe = 0x00
				smbus.write_byte_data(0x20,0x15,0x01) # Start LED an	
				lock.release()
				t_game = Process(target=running, args=())
				game_running = True
				#t_game.daemon = True
				t_game.start()
				sleep(2)
			
       	 	sleep(.01)

def running():
	#inits()

	print "running"
	global boost_active, game_running


	#Button warter starten
	tb0 = Process(target=boost_wait_b0, args=())
	#tb0.daemon = True
	tb0.start()

	tb1 = Process(target=boost_wait_b1, args=())
	#tb1.daemon = True
	tb1.start()

	tb2 = Process(target=boost_wait_b2, args=())
	#tb2.daemon = True
	tb2.start()

	tb3 = Process(target=boost_wait_b3, args=())
	#tb3.daemon = True
	tb3.start()

	tb4 = Process(target=boost_wait_b4, args=())
	#tb4.daemon = True
	tb4.start()

	tb5 = Process(target=boost_wait_b5, args=())
	#tb5.daemon = True
	tb5.start()

	tb6 = Process(target=boost_wait_b6, args=())
	#tb6.daemon = True
	tb6.start()

	tb7 = Process(target=boost_wait_b7, args=())
	#tb7.daemon = True
	tb7.start()

	while True:
		if not game_running:
			print "hoer auf"
			pwm1A .ChangeDutyCycle(0)
			pwm1B .ChangeDutyCycle(0)
			tb0.terminate()
			tb1.terminate()
			tb2.terminate()
			tb3.terminate()
			tb4.terminate()
			tb5.terminate()
			tb6.terminate()
			tb7.terminate()
			return
		if clockwise == 5:
        	       	pwm1B .ChangeDutyCycle(0)                                        
			if boost_active:
				print "Booster"
				pwm1A .ChangeDutyCycle(100)
				sleep(.7)
				boost_active = False
			else:
				pwm1A .ChangeDutyCycle(speed)                                    
               		#print "Going forwards with ", speed, "%"                         
               		GPIO.output(Motor1A,GPIO.HIGH)                                           
                	GPIO.output(Motor1B,GPIO.LOW)                                            
                	GPIO.output(Motor1E,GPIO.HIGH)          
		else:
	        	pwm1A .ChangeDutyCycle(0)                                                        
			if boost_active:
				print "Booster"
				pwm1B .ChangeDutyCycle(100)
				sleep(.7)
				boost_active = False
			else: 
				pwm1B .ChangeDutyCycle(speed)                                                    
	        	GPIO.output(Motor1A,GPIO.LOW)                                                    
	        	GPIO.output(Motor1B,GPIO.HIGH)                                                   
	        	GPIO.output(Motor1E,GPIO.HIGH)     
		sleep(.1)

def end(): 
	global Motor1E,pwm1A,pwm1B
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	pwm1A.stop()
	pwm1B.stop()
	GPIO.cleanup()

def change_speed():
	global speed, hexe
	while True:
		#with lock:
		speed = randint(25,50)
		print "Speed im Thread ist", speed
		print "hexe ist", hexe
		sleep(randint(2,10))

def change_direction():
	global clockwise
        while True:                
		clockwise = randint(0,10)
		if clockwise == 5:
			print "rueck" , clockwise
			sleep(randint(5,10))
		else:
			print "vor", clockwise
                	sleep(randint(10,20))
                
t_speed = Process(target=change_speed, args=())
t_speed.daemon = True
t_speed.start()

t_direc = Process(target=change_direction, args=())
t_direc.daemon = True   
t_direc.start()       

while True:
	t = Process(target=pressed_bstart, args=())
	#t.daemon = True
	t.start()
	t.join()
	print "stop gedrueckt"
	sleep(.01)
	
	smbus.write_byte_data(0x20,0x14,0x00) # Bank A alle aus
	
	#Stop gedrueckt
	#aufraeumen
	#end()
	#wieder neu starten und warten
end()
