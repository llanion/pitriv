import RPi.GPIO as GPIO
import pygame.mixer
from time import sleep

# Define input pins for the different buttons
BTN_CLEAR=26
BTN_WHITE=10
BTN_BLUE=16
BTN_GREEN=22

#Define output pins (for the LEDs)
LED_WHITE=11
LED_BLUE=19
LED_GREEN=23

#Right now we want to accept any button press
lock=False

pygame.mixer.init()


def button_callback(channel):
#	This sets the 'lock' variable here to be the same as the one set globally
	global lock

	if (channel == BTN_CLEAR):
		lock = False
		print("Buzzer has been cleared for input")
		GPIO.output(LED_WHITE,GPIO.LOW)
		GPIO.output(LED_BLUE,GPIO.LOW)
		GPIO.output(LED_GREEN,GPIO.LOW)
		return()

	if (lock == True):
		return()	

	lock = True

	pygame.mixer.music.load("/home/pi/jump.mp3")
	pygame.mixer.music.play(1)

	if (channel == BTN_WHITE):
		print("White button was pushed")
		GPIO.output(LED_WHITE,GPIO.HIGH)
	if (channel == BTN_BLUE):
		print("Blue button was pushed")
		GPIO.output(LED_BLUE,GPIO.HIGH)
	if (channel == BTN_GREEN):
		print("Green button was pushed")
		GPIO.output(LED_GREEN,GPIO.HIGH)

#Main program setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Set up the LED pins as outputs
GPIO.setup(LED_WHITE,GPIO.OUT)
GPIO.setup(LED_BLUE,GPIO.OUT)
GPIO.setup(LED_GREEN,GPIO.OUT)

#Set up the GPIO pins for the buttons as inputs
GPIO.setup(BTN_CLEAR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_WHITE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Listen for button pushes on those pins
GPIO.add_event_detect(BTN_CLEAR,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.add_event_detect(BTN_WHITE,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.add_event_detect(BTN_BLUE,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.add_event_detect(BTN_GREEN,GPIO.RISING,callback=button_callback,bouncetime=200)

# Light all three lights to show that the program is ready
GPIO.output(LED_WHITE,GPIO.HIGH)
GPIO.output(LED_BLUE,GPIO.HIGH)
GPIO.output(LED_GREEN,GPIO.HIGH)

# Because there's no keyboard, this will wait forever for someone to press enter.
message = input("Press enter to quit\n\n")

#Clean up after yourself on the way out!
GPIO.cleanup()
