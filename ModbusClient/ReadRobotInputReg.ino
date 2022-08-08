long ReadRobotInputReg(int Reg){
  long RobotRegValue;
  ROBOTClient.begin(serverRobot,502);
 
  RobotRegValue = ROBOTClient.inputRegisterRead(Reg);
  ROBOTClient.end();
  ROBOTClient.stop();
  delayMicroseconds(100);
  //Serial.println(RobotRegValue);
  return RobotRegValue;
}
