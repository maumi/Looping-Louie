import RPi.GPIO as GPIO
from time import sleep
from random import randrange,randint
from threading import Thread,Lock

#global speed
speed = 20
#global clockwise
clockwise = 1
lock = Lock()
button_active = False
boost_active = False
game_running = True

#vor 
Motor1A = 16
#zurueck
Motor1B = 18
#an
Motor1E = 22

GPIO.setmode(GPIO.BOARD)

def inits(): 
	#Nummerierung wie PINS auf dem Board
	#GPIO.setmode(GPIO.BOARD)

	#alles ausgaenge 
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
	global pwm1A,pwm1B
	# we set the PWM controller to Motor1A for forward movement with 250 Hz frequency
	pwm1A = GPIO.PWM( Motor1A, 250 ) 
	# we do the same for Motor1B (for reverse movement)
	pwm1B = GPIO.PWM( Motor1B,250 )

	# we start both pwm controllers to zero duty cycle( off )
	pwm1A.start( 0 )
	pwm1B.start( 0 )

def button_init():
	#GPIO.setmode(GPIO.BOARD)

	# Die 9 LEDs raussuchen und ausschalten
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, False)  
	
	# Die 9 Buttons als Eingaenge
	GPIO.setup(13, GPIO.IN)
		
def boost_wait_b0():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b0, args=())
		t.daemon = True
		t.start()
		t.join()
		
def boost_wait_b1():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b1, args=())
		t.daemon = True
		t.start()
		t.join()

		
def boost_wait_b2():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b2, args=())
		t.daemon = True
		t.start()
		t.join()

		
def boost_wait_b3():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b3, args=())
		t.daemon = True
		t.start()
		t.join()
		
def boost_wait_b4():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b4, args=())
		t.daemon = True
		t.start()
		t.join()
		
def boost_wait_b5():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b5, args=())
		t.daemon = True
		t.start()
		t.join()
		
def boost_wait_b6():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b6, args=())
		t.daemon = True
		t.start()
		t.join()
			
def boost_wait_b7():
	while True:
		sleep(randint(10,20))
		# LED von Taster 0 aktivieren
		
		# Button Boost Thread aktivieren
		t = Thread(target=pressed_b7, args=())
		t.daemon = True
		t.start()
		t.join()
	
def pressed_b0():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)
        
def pressed_b1():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)
        
def pressed_b2():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)

def pressed_b3():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)

def pressed_b4():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)

def pressed_b5():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)
        
def pressed_b6():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)
        
def pressed_b7():
	global boost_active
	#button_init()
	button_gpio = 11
	if boost_active:
		#LED aus
		GPIO.output(button_gpio, False)	
		return
	while True:
		if not (GPIO.input(button_gpio)):			
			boost_active = True	
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)		
        sleep(.1)
        
def pressed_bstart():
	global game_running
	#button_init()
	GPIO.setup(11, GPIO.OUT)
	button_gpio = 11
	while True:
		if not (GPIO.input(button_gpio)):	
			if game_running:	
				#Spiel stoppen
				return
			elif not game_running:
				#Spiel Starten
				t_game = Thread(target=running, args=())
				t_game.daemon = True
				t_game.start()
				game_running = True

			
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)
        	sleep(.2)        
        	GPIO.output(button_gpio, False)
        	sleep(.2)       
        	GPIO.output(button_gpio, True)			
        	sleep(.2)        
        	GPIO.output(button_gpio, False)	
        	
        sleep(.1)

def running():
	inits()

	global boost_active
	while True:
		if clockwise == 1:
			#with lock:
			if boost_active:
				print "Booster"
				pwm1A .ChangeDutyCycle(100)
			else:
				pwm1A .ChangeDutyCycle(speed)                                    
        	       	pwm1B .ChangeDutyCycle(0)                                        
               		#print "Going forwards with ", speed, "%"                         
               		GPIO.output(Motor1A,GPIO.HIGH)                                           
                	GPIO.output(Motor1B,GPIO.LOW)                                            
                	GPIO.output(Motor1E,GPIO.HIGH)          
		else:
	        	pwm1A .ChangeDutyCycle(0)                                                        
			#with lock:
			if boost_active:
				print "Booster"
				pwm1B .ChangeDutyCycle(100)
			else: 
				pwm1B .ChangeDutyCycle(speed)                                                    
	        	#print "Going backwards with ", speed, "%"                                        
	        	GPIO.output(Motor1A,GPIO.LOW)                                                    
	        	GPIO.output(Motor1B,GPIO.HIGH)                                                   
	        	GPIO.output(Motor1E,GPIO.HIGH)     
		sleep(.1)

def end(): 
	global Motor1E
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	pwm1A.stop()
	pwm1B.stop()
	GPIO.cleanup()


def change_speed():
	global speed
	while True:
		#with lock:
		speed = randint(0,80)
		print "Speed im Thread ist", speed
		sleep(randint(2,10))

def change_direction():
	global clockwise
        while True:                
                clockwise = randint(0,1)
                sleep(randint(4,10))
                
t_speed = Thread(target=change_speed, args=())
t_speed.daemon = True
t_speed.start()

t_direc = Thread(target=change_direction, args=())
t_direc.daemon = True   
t_direc.start()       

while True:
	t = Thread(target=pressed_bstart, args=())
	t.daemon = True
	t.start()
	t.join()
	
	#Stop gedrueckt
	#aufraeumen
	#end()
	#wieder neu starten und warten


#sleep(20)
end()