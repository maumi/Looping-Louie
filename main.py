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

def inits(): 
	#Nummerierung wie PINS auf dem Board
	GPIO.setmode(GPIO.BOARD)

	global Motor1A, Motor1B, Motor1E
	#vor 
	Motor1A = 16
	#zurueck
	Motor1B = 18
	#an
	Motor1E = 22

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
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, False)  
	GPIO.setup(13, GPIO.IN)

def button_wait():
	global button_active
	global boost_active
	button_init()
	while True:                     
        	if not (GPIO.input(13)) and button_active:      
                	GPIO.output(11, False)
                	sleep(.1)       
                	GPIO.output(11, True)
                	sleep(.1)        
                	GPIO.output(11, False)
                	sleep(.1)       
                	GPIO.output(11, True)
  			#boost anschalten 
			boost_active = True			
			#dann knopf deaktivieren
			button_active = False
			GPIO.output(11, False) 
			sleep(5)
			boost_active = False

def boost_wait():
	global button_active
	while True:
		sleep(10)
		GPIO.output(11, True)
		button_active = True

"""
def forward():
	inits()
	while True:
		with lock:
			pwm1A .ChangeDutyCycle(speed)
			pwm1B .ChangeDutyCycle(0)
			print "Going forwards with ", speed, "%"
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)
		sleep(1)	

def backward(speed): 
        pwm1A .ChangeDutyCycle(0)                                            
        pwm1B .ChangeDutyCycle(speed) 
	print "Going backwards with ", speed, "%"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	sleep(6)	
"""

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
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	pwm1A.stop()
	pwm1B.stop()
	GPIO.cleanup()

def change_speed():
	global speed
	while True:
		#with lock:
		speed = randint(0,100)
		print "Speed im Thread ist", speed
		#sleep(2)
		sleep(randint(2,10))

def change_direction():
	global clockwise
        while True:                
                clockwise = randint(0,1)
		#sleep(4)
                sleep(randint(2,10))

t = Thread(target=running, args=())
t.daemon = True
t.start()

t_speed = Thread(target=change_speed, args=())
t_speed.daemon = True
t_speed.start()

t_direc = Thread(target=change_direction, args=())
t_direc.daemon = True   
t_direc.start()       

t_button_wait = Thread(target=button_wait, args=())                                 
t_button_wait.daemon = True                                                          
t_button_wait.start()                  

t_boost_wait = Thread(target=boost_wait, args=())                             
t_boost_wait.daemon = True                                                     
t_boost_wait.start()  

sleep(20)
end()

