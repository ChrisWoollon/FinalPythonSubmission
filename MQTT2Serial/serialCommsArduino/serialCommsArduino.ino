int ledPin = 13;
int ledPin2 = 12;
boolean ledOn = false;
void setup() {
  
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  
}

void loop() {
 
  if(Serial.available()>0) {
    char command = Serial.read();
    if(command == '1') ledOn = true;
    else if(command == '0') ledOn = false;
  }
  
  if (ledOn == true) 
  {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin2, LOW);
  }
  else if (ledOn == false) 
  {
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, HIGH);

  }
}
