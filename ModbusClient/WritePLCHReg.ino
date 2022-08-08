void WritePLCHReg(int Reg, long Value){
  long PLCReg;
  PLCClient.begin(serverPLC,502);
   
  if(PLCClient.connected()){
    //Serial.println("Conectado ao PLC");
    PLCReg = PLCClient.holdingRegisterWrite(Reg,Value);
    
    
    PLCClient.end();
    PLCClient.stop();
    delayMicroseconds(100);
  
  }
}
