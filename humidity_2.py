import time
import serial
from vpython import*
import numpy as np

arduinoData=serial.Serial('com3',115200)
time.sleep(.5)

boxX=10
boxY=6
boxZ=.4
offsetRight=boxX/2+2
myCase = box(size=vector(boxX,boxY,boxZ),color=color.white,pos=vector(offsetRight,0,-boxZ/2))

arrowLength=boxY-2
arrowThickness=.15
arrowZoff = 0.25
myArrow=arrow(Length=arrowLength,color=color.red,shaftwidth=arrowThickness,pos=vector(offsetRight,(-boxY/2)*0.9,arrowZoff))

tickL=.4
tickW=.07
tickH=.07
tickF=.7
for theta in np.linspace(5*np.pi/6,np.pi/6,11):
    tickMajor=box(pos=vector(1.1*arrowLength*np.cos(theta)+offsetRight,1.1*arrowLength*np.sin(theta)-.9*boxY/2,0),size=vector(tickL,tickW,tickH),color=color.black,
    axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))

for theta in np.linspace(5*np.pi/6,np.pi/6,51):
    tickMinor=box(pos=vector(1.1*arrowLength*np.cos(theta)+offsetRight,1.1*arrowLength*np.sin(theta)-.9*boxY/2,0),
    size=vector(tickF*tickL,tickF*tickW,tickF*tickH),color=color.black,
    axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0))

num=0
for theta in np.linspace(5*np.pi/6,np.pi/6,11):
    lab=text(text=str(num),pos=vector(1.1*arrowLength*np.cos(theta)+offsetRight,1.2*arrowLength*np.sin(theta)-.9*boxY/2,0),
    ,axis=vector(arrowLength*np.cos(theta-np.pi/2),arrowLength*np.sin(theta),0),color=color.black,height=.4,align='cener')
    num=num=+10

digValue = label(text='50',height=20,box=False,pos=vecetor(0,-2.5,2))
bulb = sphere(radius=1,color=color.red,pos=vector(0,-3,0))
cyl = cylinder(radius=.6,color=color.red,axis=vector(0,1,0),length=6,pos=vector(0,-3,0))
bulbGlass = sphere(radius=1.2,color=color.white,opacity=.25,pos=vector(0,-3,0))
cylGlass = cylinder(radius=.8,color=color.white,axis=vector(0,1,0),opacity=0.25,length=6,pos=vector(0,-3,0))
for temp in range(0,115,10):
    tickPos=4.5/115*temp+1.5
    tick = cylinder(radius=.7,color=color.black,Length=.1,axis=vector(0,1,0),pos=vector(0,tickPos-3,0))
    label = text(text=str(temp),color = color.white,pos=vector(-2,tickPos-3,0),height=.3)

while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=int(dataPacket.strip('\r\n'))
    dataPacket = dataPacket.split(',')
    temp=float(dataPacket[0])
    hum=float(dataPacket[1])

    len = (4.5/115)*temp+1.5
    cyl.length = len
    digValue.text = str(temp)
    theta=-np.pi/150*hum+5*np.pi/6
    myArrow.axis = vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)