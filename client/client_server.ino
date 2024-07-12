#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

float tempF;
float tempC;
float humidity;

int setTime = 500;
int dt = 1000;

String cmd;

DHT TH(DHTPIN,DHTTYPE);

void setup() {
  // put your setup code here, to run once:
Serial.begin(1115200);
TH.begin();
delay(setTime);

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()==0){

  }
  cmd=Serial.readStringUntil('\r')
  if (cmd="temp"){
    tempF = TH.readTemperature(true);
    Serial.print("Temp:")
    Serial.println(tempF);
    
  }
  if (cmd="humidity"){
    Serial.print("Humidity:")
    humidity = TH.readHumidty();
    Serial.println(humidity);
  }

Serial.print(tempF);
Serial.print("Degree F,");
Serial.print(tempC);
Serial.print("Degree C,");
Serial.print(humidity);
Serial.print("% Humidity");

delay(dt);


}
