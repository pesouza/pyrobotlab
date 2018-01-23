# sync-servos movements with servos connected with myrobotlab AdaFruit16C servo service
# Acapulco Rolf
# 26 12 2017

from time import sleep

adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver");

#start a Raspberry Pi instance
raspi = Runtime.createAndStart("RasPi","RasPi");

#attach the AdaFruit16C I2C servo driver to the Raspberry Pi
adaFruit16c.setController("RasPi","1","0x40");

#set the frequency for the AdaFruit16C I2C servo driver to 50 Hz
adaFruit16c.setPWMFreq(0,50);

servoPin1 = 12
servoPin2 = 15

servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")

servo01.attach(adaFruit16c,servoPin1,90,-1);
servo02.attach(adaFruit16c,servoPin2,90,-1);

servo02.sync(servo01)

def servoMoveTo(restPos,delta):
	servo01.moveTo(restPos + delta)
	#servo02.moveTo(restPos + delta)
	servo01.broadcastState()
	#servo02.broadcastState()
	
	
#servo02.addServoEventListener(servo01)
#servo02.eventsEnabled(True)
#servo01.eventsEnabled(True)
#servo02.moveTo(90)

restPos = 45
delta = 0

def moveservos():
	for x in range (1,5):
		for i in range (10,160,5):
			servoMoveTo(restPos,i)
			#servo01.moveTo(i)
			#sleep for a bit	
			sleep(0.25)
			#update servo GUI with current servo position	
			#sleep for a bit
			sleep(0.25)

		for i in range (160,10,-5):
			servoMoveTo(restPos,i)
			#servo01.moveTo(i)
			#sleep for a bit	
			sleep(0.25)


for y in range(10,160,5):
	servo01.moveTo(y)
	sleep(0.25)
	servo01.broadcastState()

for y in range(160,10,-5):
	servo01.moveTo(y)
	sleep(0.25)
	servo01.broadcastState()
	
	