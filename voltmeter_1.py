import time
import serial
from vpython import*
import numpy as np
tickL=.1
tickW = .05
tickH=.05
arrowLength = 1
arrowWidth = .02
myArrow = arrow(length=arrowLength,shaftwidth= arrowWidth,color=color.red,axis=vector(1,1,0))
arduinoData=serial.Serial('com3',115200)

for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor=box(pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL,tickW,tickH))


time.sleep(1)
boxX=2.5
boxY=1.5
boxZ=.1
myCase = box(color = color.white,size=vector(boxX,boxY,boxZ),pos=vector(0.0,-boxZ))




while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=int(dataPacket.strip('\r\n'))
    potVal=dataPacket
    theta = -2*np.pi/3069*potVal+5*np.pi/6
    myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    for theta in np.linspace(5*np.pi/6,np.pi/6,150):
        rate(25)
        myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta))
    
    for theta in np.linspace(np.pi/6,5*np.pi/6,150):
        rate(25)
        myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta))


