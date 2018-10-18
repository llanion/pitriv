import RPi.GPIO as GPIO
import pygame.mixer
from time import sleep
BTN_CLEAR=26
BTN_WHITE=10
BTN_BLUE=16
BTN_GREEN=22
LED_WHITE=11
LED_BLUE=19
LED_GREEN=23
lock=False
pygame.mixer.init()
def button_callback(channel):
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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_WHITE,GPIO.OUT)
GPIO.setup(LED_BLUE,GPIO.OUT)
GPIO.setup(LED_GREEN,GPIO.OUT)
GPIO.setup(BTN_CLEAR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BTN_CLEAR,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.setup(BTN_WHITE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BTN_WHITE,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.add_event_detect(BTN_BLUE,GPIO.RISING,callback=button_callback,bouncetime=200)
GPIO.add_event_detect(BTN_GREEN,GPIO.RISING,callback=button_callback,bouncetime=200)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
