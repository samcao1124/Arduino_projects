import serial 
from vpython import *
arduinoData = serial.Serial('com3',115200)
baseRadius=1
baseHeight=baseRadius/5
bodyRadius=baseRadius*.75
bodyHeight=2.5*bodyRadius
LEDTopRadius = baseRadius
LEDTopPos = vector(0,bodyHeight,0)
bulbRadius= bodyRadius*.75
Leg1Length=8*bodyRadius
Leg2Length=10*bodyRadius
Leg3Length=9*bodyRadius
Leg4Length=8*bodyRadius
legWidth=baseRadius/10
bulbOpacity = bulbOpacity / 2
bottomOpacity = bulbOpacity/5
bulbPos=LEDTopPos
myColor = vector(10:10:10)
myAxis=vector(0,1,0)
LEDBase=cylinder(Length=baseHeight,radius=baseRadius,color=myColor,axis=myAxis,opacity=bottomOpacity)
LEDBody=cylinder(Length=bodyHeight,radius=bodyRadius,color=myColor,axis=myAxis,opacity=bottomOpacity)
LEDTop=sphere(radius=LEDTopRadius,color=myColor,pos=LEDTopPos,opacity=topOpacity)

bulb = sphere(radius=bulbRadius,color=myColor,pos=bulbPosopacity=bulbOpacity)
leg1-box(color=color.white,axis=myAxis,pos=vector(-0.5*baseRadius,-Leg1Length/2+baseHeight,0),Length=Leg1Length,width=legWidth,height=legWidth)
leg2-box(color=color.white,axis=myAxis,pos=vector(-0.15*baseRadius,-Leg2Length/2+baseHeight,0),Length=Leg2Length,width=legWidth,height=legWidth)
leg3-box(color=color.white,axis=myAxis,pos=vector(0.15*baseRadius,-Leg3Length/2+baseHeight,0),Length=Leg3Length,width=legWidth,height=legWidth)
leg4-box(color=color.white,axis=myAxis,pos=vector(0.5*baseRadius,-Leg4Length/2+baseHeight,0),Length=Leg4Length,width=legWidth,height=legWidth)

head = compound([bulb,LEDBase,LEDBody,LEDTop])

while True:
    myCmd=input("Please Input Your Color R:G:G 0-255 ")
    myCmd = myCmd+'\r'
    arduinoData.write(myCmd.encode())
    myColor = myCmd.split(':')
    red = int(myColor[0])
    green = int(myColor[1])
    blue = int(myColor[2])
    head.color=vector(red/255,green/255,blue/255)