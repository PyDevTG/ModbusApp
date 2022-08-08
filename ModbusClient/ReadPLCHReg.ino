long ReadPLCHReg(int addr,int Reg){
  long PLCReg;
  PLCClient.begin(serverPLC,502);
  if(PLCClient.connected()){
   
    //Serial.println("Conectado ao PLC");
    PLCReg = PLCClient.holdingRegisterRead(addr,Reg);
    //Serial.println(PLCReg);
    //Serial.println(PLCClient.lastError());
    PLCClient.end();
    PLCClient.stop();
    delayMicroseconds(100);
   return PLCReg;
  }
  
}
