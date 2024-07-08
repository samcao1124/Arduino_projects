int redPin = 11;
int greenPin = 10;
int bluePin =9;
int redVal = 255;
int greeVal = 255;
int blueVal = 255;
String cmd;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(redPin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(bluePin,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() == 0){

  }
  redVal = Serial.readStringUnit('.').tolnt();
  greenVal = Serial.readStringUnit('.').tolnt();
  blueVal = Serial.readStringUnit('\r').tolnt();

  cmd = Serial.readstringUnit("\r");
  if(cmd=="RED"){
    analogWrite(redPin,redVal);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  }
  if(cmd=="GREEN"){
    analogWrite(redPin,0);
    analogWrite(greenPin,greenVal);
    analogWrite(bluePin,0);
  }
  if(cmd=="BLUE"){
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,blueVal);
  }
  if(cmd=="CYAN"){
    analogWrite(redPin,0);
    analogWrite(greenPin,greenVal);
    analogWrite(bluePin,blueVal);
  }
   if(cmd=="MAGENTA"){
    analogWrite(redPin,redVal);
    analogWrite(greenPin,0);
    analogWrite(bluePin,blueVal);
  }
   if(cmd=="YELLOW"){
    analogWrite(redPin,redVal);
    analogWrite(greenPin,greenVal);
    analogWrite(bluePin,0);
  }

  if(cmd=="ON"){
    analogWrite(redPin,redVal);
    analogWrite(greenPin,greenVal);
    analogWrite(bluePin,blueVal);
  }
  if(cmd=="OFF"){
    analogWrite(redPin,0);
    analogWrite(bluePin,0);
    analogWrite(greenPin,0);
    
  }
  analogWrite(redPin,redVal);
  analogWrite(greenPin,greenVal);
  analogWrite(bluePin,blueVal);

}
