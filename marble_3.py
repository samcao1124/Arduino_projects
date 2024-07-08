from vpython import *
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

marbleX=0
deltaX=.1

marbleY=0
deltaT=.1

marbleZ=0
deltaZ=.1



while True:
    rate(20)
    marbleX=marbleX+deltaX
    marbleY=marbleY+deltaY
    marbleZ=marbleZ+deltaZ
    if marbleX + marbleR > (roomX/2 - wallT/2) or marbleX=marbleR<(-roomX/2+wallT/2):
        deltaX=deltaX*(-1)
        marbleX=marblex+deltaX
    if marbleY + marbleR > (roomY/2 - wallT/2) or marbleY=marbleR<(-roomY/2+wallT/2):
        deltaY=deltaY*(-1)
        marbleY=marbleY+deltaY
     if marbleZ + marbleR > (roomZ/2 - wallT/2) or marbleZ=marbleR<(-roomZ/2+wallT/2):
        deltaZ=deltaZ*(-1)
        marbleZ=marbleZ+deltaZ
    marble.pos=vector(marbleX,marbleY,marbleZ)