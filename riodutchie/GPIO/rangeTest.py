import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24
POUR=4
print "Distance Measurement in Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print "Waiting for sensor to Settle"
time.sleep(2)

distance = 10

while (distance >= 1):
   GPIO.output(TRIG,True)
   time.sleep(0.00001)
   GPIO.output(TRIG,False)
   while GPIO.input(ECHO)==0:
      pulse_start = time.time()
   while GPIO.input(ECHO)==1:
      pulse_end = time.time()
   pulse_duration = pulse_end - pulse_start
   distance = pulse_duration * 6771.65
   distance = round(distance,2)
   if(distance >= 4):
      print "Move Closer, distance=",distance," in"
      time.sleep(0.5)
   elif(distance <= 4) and (distance > 2):
      print "BEEEERRR! distance=",distance," in"
      print "Pouring for ",POUR," seconds"
      time.sleep(4.0)
      print "Move away and give the next person a chance..."
      time.sleep(1.0)
   elif(distance <= 2):
      print "Time to exit, distance is ",distance," in"
      break
   else:
      print "Not sure what to do, distance is ",distance," in - quitting"
      break

   time.sleep(0.5)

print "Distance is: ",distance," in"

GPIO.cleanup()
