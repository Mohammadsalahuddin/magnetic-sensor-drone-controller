# drone flying program


#########
# firstTry.py
# This program is part of the online PS-Drone-API-tutorial on www.playsheep.de/drone.
# It shows how to do basic movements with a Parrot AR.Drone 2.0 using the PS-Drone-API.
# Dependencies: a POSIX OS, PS-Drone-API 2.0 beta or higher.
# (w) J. Philipp de Graaff, www.playsheep.de, 2014
##########
# LICENCE:
#   Artistic License 2.0 as seen on http://opensource.org/licenses/artistic-license-2.0 (retrieved December 2014)
#   Visit www.playsheep.de/drone or see the PS-Drone-API-documentation for an abstract from the Artistic License 2.0.
###########
import serial
import os

import RPi.GPIO as GPIO
import time
import ps_drone                # Imports the PS-Drone-API


# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyACM0'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
value = 0.0 

def data():
	ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
# using ser.readline() assumes each line contains a single reading
# sent using Serial.println() on the Arduino
	reading = ser.readline().decode('utf-8')
# reading is a string...do whatever you want from here
# time.sleep(2)        
	print(reading)
	value = float(reading)
	print value
	if value  > 0.0:
		print 'Left Rotation'
#                   os.system('pico2wave -w audio.wav "The water is up." && aplay lookdave.wav')
	else:
		print 'Right Rotation'
#                    os.system('pico2wave -w audio.wav "The water is down." && aplay lookdave.wav')
	time.sleep(1)
	ser.close()

	return value



def my_callback(channel):
	if GPIO.input(6) == GPIO.HIGH:
		print('\n Take off the Drone\n')
		drone.takeoff()                # Drone starts
		time.sleep(8)                # Gives the drone time to start
	elif GPIO.input(23) == GPIO.HIGH:
		print('\n Landing  \n')
		drone.land()                   # Drone lands
		time.sleep(1)
	elif GPIO.input(24) == GPIO.HIGH:
		print('\n Rotation\n ')
		#read the serial data first 
		deg = data()
		if deg > 0.0:
			drone.turnLeft()               # Drone moves full speed to the left...
			time.sleep(3)                  # ... for two seconds
			drone.stop()                   # Drone stops
			time.sleep(2)
		else:
			drone.turnRight()               # Drone moves full speed to the left...
			time.sleep(3)                  # ... for two seconds
			drone.stop()                   # Drone stops
			time.sleep(2)	


drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(6, GPIO.RISING, callback=my_callback)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback)
	GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)
 
	message = raw_input('\nPress any key to exit.\n')
 
finally:
	GPIO.cleanup()
 
print("Goodbye!")



