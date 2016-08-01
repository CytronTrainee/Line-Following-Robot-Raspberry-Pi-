import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
AN2 = 25
AN1 = 24
DIG2 = 23
DIG1 = 18
GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(AN1, GPIO.OUT)
GPIO.setup(DIG2, GPIO.OUT)
GPIO.setup(DIG1, GPIO.OUT)
GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(9, GPIO.IN)     #SO2
GPIO.setup(10, GPIO.IN)    #S03
GPIO.setup(22, GPIO.IN)    #SO4
GPIO.setup(27, GPIO.IN)    #SO5
sleep(1)
p1 = GPIO.PWM(AN1, 100)
p2 = GPIO.PWM(AN2, 100)

#on = black, off = white

try:
  while True:
    s1=GPIO.input(11)
    s2=GPIO.input(9)
    s3=GPIO.input(10)
    s4=GPIO.input(22)
    s5=GPIO.input(27)
    def forward():
      GPIO.output(DIG1, GPIO.HIGH)
      GPIO.output(DIG2, GPIO.HIGH)
#10000
    if (s1==1)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
      print "left1"
      forward()
      p1.start(20)
      p2.start(0)
      sleep(0.5)
#11000
    elif (s1==1)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
      print "left2"
      forward()
      p1.start(20)
      p2.start(5)
      sleep(0.5)
#11100
    elif (s1==1)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
      print "left3"
      forward()
      p1.start(20)
      p2.start(7.5)
      sleep(0.5)
#01000    
    elif (s1==0)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
      print "left4"
      forward()
      p1.start(20)
      p2.start(9)
      sleep(0.5)
#01100
    elif (s1==0)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
      print "left5"
      forward()
      p1.start(20)
      p2.start(14)
      sleep(0.5)
#00001
    elif (s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==1):
      print "right1"
      forward()
      p1.start(0)
      p2.start(20)
      sleep(0.5)
#00011
    elif (s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==1):
      print "right2"
      forward()
      p1.start(5)
      p2.start(20)
      sleep(0.5)
#00111
    elif (s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==1):
      print "right3"
      forward()
      p1.start(7.5)
      p2.start(20)
      sleep(0.5)
#00010
    elif (s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==0):
      print "right4"
      right()
      p1.start(9)
      p2.start(20)
      sleep(0.5)
#00110
    elif (s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==0):
      print "right5"
      forward()
      p1.start(12)
      p2.start(20)
      sleep(0.5)
#00100
    elif (s1==0)and(s2==0)and(s3==1)and(s4==0)and(s5==0):
      print "straight1"
      forward()
      p1.start(20)
      p2.start(20)
      sleep(0.5)
#01110
    elif (s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
      print "straight2"
      forward()
      p1.start(20)
      p2.start(20)
      sleep(0.5)
    else:
      print "stop"
      GPIO.output(AN1, GPIO.LOW)
      GPIO.output(AN2, GPIO.LOW)
except:
  p1.start(0)
  p2.start(0)
