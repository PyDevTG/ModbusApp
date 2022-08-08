
#include <SPI.h>
#include <Ethernet.h>

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>
long RobotReg;
long PLCReg;
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 0, 121);

EthernetClient Plc_Client,Robot_Client;
ModbusTCPClient PLCClient(Plc_Client);
ModbusTCPClient ROBOTClient(Robot_Client);

IPAddress serverPLC(192, 168, 0, 10); // update with the IP Address of your Modbus server
IPAddress serverRobot(192, 168, 0, 30); // update with the IP Address of your Modbus server

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }
   //PLCClient.begin(serverPLC,502);
   ROBOTClient.begin(serverRobot,502); 
}

void loop() {
 
  long HregActualValue = 0;
  long InputsRobotTOPlc =0;
  
 for (int i=500,j=31 ; i<510,j<41;i++,j++){
  HregActualValue = ReadPLCHReg(2,i);
  WriteRobotHreg(j,HregActualValue);
 }
 for (int a = 600,b=31;a<610,b<41;a++,b++){
  InputsRobotTOPlc = ReadRobotInputReg(b);
  WritePLCHReg(a, InputsRobotTOPlc);
  
 }
WritePLCHReg(450, 1);

  
}
