/*
  This Example is to create a Modbus TCP Server using arduino with ethernet shield W5100 
  Author: Eng Thiago Alves
  is based on the example from Arduino Modbus Server.
*/

#include <SPI.h>
#include <Ethernet.h>

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>


// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 0, 10);

EthernetServer ethServer(502);// Communication Port

ModbusTCPServer modbusTCPServer;



bool Reset=false;
long Reg0 = modbusTCPServer.holdingRegisterRead(10);
const int ledPin = LED_BUILTIN;
void(* resetFunc) (void) = 0; //declare reset function @ address 0
void setup() {
  Serial.begin(9600);
  for (int i=0;i<100;i++){
  delay(100);
  Serial.print("*");
  
}
Serial.println("*");
Serial.println("Iniciando a controladora");
 pinMode(ledPin,OUTPUT);
 
  
  
  Serial.println("Ethernet Modbus TCP Server");

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  Ethernet.init();
  Serial.println("Ethernet W5100 Starting..");

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    
    }
  
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  // start the server
  ethServer.begin();
  
  // start the Modbus TCP server
  if (!modbusTCPServer.begin()) {
    Serial.println("Failed to start Modbus TCP Server!");
    ethServer.begin();
   
  }


 //COnfigure a single reg
  modbusTCPServer.configureHoldingRegisters(0x00,100);
//Waiting to start Ethernet Shield
 

}

void loop() {
 

  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
    //resetFunc();  //call reset
    //Ethernet.init();
  }
  // listen for incoming clients
  EthernetClient client = ethServer.available();
  
  if (client) {
    // a new client connected
    Serial.println("new client");

    // let the Modbus TCP accept the connection 
    modbusTCPServer.accept(client);
    

    if (client.connected()) {
      
      // poll for Modbus TCP requests, while client connected
      modbusTCPServer.poll();

      readHoldingReg();
      updateLED();
      delay(10);
      
    }

    Serial.println("client disconnected");
    
  }
}
void readHoldingReg(){
  Reg0 = modbusTCPServer.holdingRegisterRead(10);
  //Leituras analógicas
  modbusTCPServer.holdingRegisterWrite(10,analogRead(A0));
  modbusTCPServer.holdingRegisterWrite(11,analogRead(A1));
  modbusTCPServer.holdingRegisterWrite(12,analogRead(A2));
  modbusTCPServer.holdingRegisterWrite(13,analogRead(A3));
  modbusTCPServer.holdingRegisterWrite(14,analogRead(A4));
  modbusTCPServer.holdingRegisterWrite(15,analogRead(A5));
  //modbusTCPServer.holdingRegisterWrite(10,100);"
  
  delay(5);
 
}
void updateLED() {
  // read the current value of the coil
  int RegValue = modbusTCPServer.holdingRegisterRead(0x00);
  Serial.println(RegValue);

  if (RegValue==1) {
    // coil value set, turn LED on
    digitalWrite(ledPin, HIGH);
  } else {
    // coild value clear, turn LED off
    digitalWrite(ledPin, LOW);
  }
}
