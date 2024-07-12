import serial
arduinoData = serial.Serial("com3",115200)



myOrb = sphere(color=color.black,radius=1)

while True:
    mycmd=input("Please Enter Your Color R:G:B 0-255: ")
    mycmd = mycmd+'\r'
    arduinoData.write(mycmd.encode())

    

    mycolor = mycmd.split(':')
    red = mycolor[0]
    green = mycolor[1]
    blue = mycolor[2]
    myOrb.color = vector(red/255,green,blue)
