import time
import serial
from vpython import*
import numpy as np


arrowLength = 1
arrowWidth = .02

myArrow = arrow(length=arrowLength,shaftwidth= arrowWidth,color=color.red,axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))

hubL = .02
hubR = .02
hub=cylinder(color=color.red,radius=hubR,Length=hubL,axis=vector(0,0,1))
tickL=.1
tickW = .02
tickH=.02


arduinoData=serial.Serial('com3',115200)

for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor=box(color = color.black,pos = vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL * tickFraction ,tickW * tickFraction,tickH* tickFraction))

tickFraction = .5
for theta in np.linspace(5*np.pi/6,np.pi/6,51):
    tickMinor=box(color = color.black,pos=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0),size=vector(tickL,tickW,tickH).axis = vector(arrowLength))

cnt =0
labF = 1.1
for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    lab = text(text =str(cnt),pos=vector(labF * arrowLength*np.cos(theta),labF *arrowLength*np.sin(theta),0),color = color.black,height= 0.1,align='center',axis = vector(arrowLength*np.cos(theta-np.pi/2),arrowLength*np.sin(theta*np.pi)/2,0))

    cnt=cnt+1

time.sleep(1)
boxX=2.5
boxY=1.75
boxZ=.1
myCase = box(color = color.white,size=vector(boxX,boxY,boxZ),pos=vector(0.0,-boxZ))

myLabel=text(text='voltomatic',pos=vector(0,1.25,0),color=color.red,height=.2.align='center')


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


