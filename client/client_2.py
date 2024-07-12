import time
import serial
from vpython import*
arduinoData=serial.Serial('com3',115200)
time.sleep(1)
tube=cylinder(color=color.blue,radius =1,length =5,axis=vector(0.1,0))#这就改掉了延申方向
lab = label(text='5 Volts',box=False,pos=vector(0,.2))


while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=int(dataPacket.strip('\r\n'))
    potVal=dataPacket
    vol=(5./1023)*potVal
    vol=round(vol,1)
    if vol ==0:
        vol = 0.001
    tube.length=vol # 会弹出来一个网页是一个条状的描述现在的voltage
    lab.text=str(vol)




