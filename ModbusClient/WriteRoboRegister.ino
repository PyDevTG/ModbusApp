void WriteRobotHreg( int Reg,long Value){
  ROBOTClient.begin(serverRobot,502); 
  if(ROBOTClient.connected()){
    //Serial.println("Conectado ao Robô");
    //D32 = ROBOTClient.coilRead(512);
    ROBOTClient.holdingRegisterWrite(Reg, Value);
       
     //Serial.println(ROBOTClient.lastError());
     ROBOTClient.end();
     ROBOTClient.stop();
     delayMicroseconds(100);
  }
}
