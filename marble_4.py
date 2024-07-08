from vpython import *
import serial
import time
import os

arduinoData=serial.Serial('com3',115200)
roomX=12
roomY=10
roomZ=16
wallT=.5
wallcolor=vector(1,1,1)
wallOpacity=.1
marbleR=.5
ballColor = vector(0,0,1)

myFloor=box(size=vector(roomX,wallT,roomZ),pos=vector(0,-roomY/2,0),color=wallcolor,opacity=wallOpacity)
myCeiling=box(size=vector(roomX,wallT,roomZ),pos=vector(0,roomY/2,0),color=wallcolor,opacity=wallOpacity)
leftWall = box(size=vector(wallT,roomY,roomZ),pos=vector(-roomX/2,0,0),color=wallcolor,opacity=wallOpacity)
rightWall = box(size=vector(wallT,roomY,roomZ),pos=vector(roomX/2,0,0),color=wallcolor,opacity=wallOpacity)
backWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,-roomZ/2),color=wallcolor,opacity=wallOpacity)
frontWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,roomZ/2),color=wallcolor,opacity=frontOpacity)
marble=sphere(color=ballColor,radius=marbleR)


paddleX=2
paddleY=2
paddleZ=.2
paddleOpacity=.8
paddleColor=vector(0,.8,.6)
paddle=box(size=vector(paddleX,paddleY,paddleZ),pos=vector(0,0,roomZ/2),color=paddleColor,opacity=paddleOpacity)





marbleX=0
deltaX=.01

marbleY=0
deltaT=.01

marbleZ=0
deltaZ=.01



while True:
    while arduinoData.in_waiting()==0:
        pass
    dataPacket=arduinoData.readline()
    print('data is: ', dataPacket)
    dataPacket= str(dataPacket,'utf-8')
    dataPacket.strip('\r\n')
    splitPacket=dataPacket.split(',')

    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])

    padX=(roomX/1023.)*x-roomX/2
    padY=(-roomY/1023.)*y-roomY/2

    marbleX=marbleX+deltaX
    marbleY=marbleY+deltaY
    marbleZ=marbleZ+deltaZ
    if marbleX + marbleR > (roomX/2 - wallT/2) or marbleX=marbleR<(-roomX/2+wallT/2):
        deltaX=deltaX*(-1)
        marbleX=marblex+deltaX
    if marbleY + marbleR > (roomY/2 - wallT/2) or marbleY=marbleR<(-roomY/2+wallT/2):
        deltaY=deltaY*(-1)
        marbleY=marbleY+deltaY
    if marbleZ=marbleR<(-roomZ/2+wallT/2):
        deltaZ=deltaZ*(-1)
        marbleZ=marbleZ+deltaZ
    if marbleZ+marbleR>=roomZ/2-wallT/2:
        if marbleX>padX-paddleX/2 and marbleX<padX+paddleX/2 and marbleY>padY-paddleY/2 and marbleY<padY+paddleY/2:
            deltaZ=deltaZ*(-1)
            marbleZ=marbleZ+deltaZ
        else:
            lb=label(text="GAME OVER!")
            time.sleep(2)
            os._exit(0)
    marble.pos=vector(marbleX,marbleY,marbleZ)
    paddle.pos=vector(padX,padY,roomZ/2)