#include <Servo.h>
#include <SoftwareSerial.h> //TX RX lib

int bluetoothTx = 10;
int bluetoothRx = 11;

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

Servo servoOne;
Servo servoTwo;

int command;

void setup() {
  // put your setup code here, to run once:
  servoOne.attach(8);
  servoTwo.attach(9);

  servoOne.write(180);
  servoTwo.write(20);
  
  Serial.begin(9600);
  bluetooth.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (bluetooth.available() > 0){
    command = bluetooth.read();
    if (command == 1){
      servoOne.write(20);
      delay(1000);
      servoOne.write(180);
    }
    else if (command == 2){
      servoTwo.write(180);
      delay(1000);
      servoTwo.write(0);
    }
  }

}
