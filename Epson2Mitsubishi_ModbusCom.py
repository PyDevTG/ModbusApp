#--------------------------------------------------------------------------------------------------------------
#------------------------- Converter Script to provide the communication between EPSON Robot to MITSUBISHI FX5u
#------------------------------------------------------------------------------------------------------------
#---- Author : Eng. Thiago ALves
#---- Date: 05/08/22 -----------
#-------------------------------------------------------------------------------------------------------------
from pyModbusTCP.client import ModbusClient
from time import sleep
import os
ipRobot='192.168.0.30'
ipPLC='192.168.0.10'
ComunicationPort=502
RegPLC =  None
RegRobot= None
RegRobot_reference = 31
RegPLC_reference = 500
Regs_qtd = 20
ConectionAliveReg=499

def StartMainRoutine():
    PLC = ModbusClient(host=ipPLC, port=ComunicationPort, auto_open=True, debug=False,unit_id=1)
    RobotEpson = ModbusClient(host=ipRobot, port=ComunicationPort, auto_open=True, debug=False,unit_id=1)


    try:
        PLC.open()
        RobotEpson.open()
        if(PLC.open()):
            print("Conectado ao PLC")
        if(RobotEpson.open()):
            print("Conectado ao Robô")
    except Exception as ex:
        print("Não foi possível conectar aos Clientes")
        pass

    

    while(True):
        PLC.write_single_register(ConectionAliveReg,1)
        RegPLC =  PLC.read_holding_registers(RegPLC_reference,Regs_qtd)
        RegRobot = RobotEpson.read_input_registers(RegRobot_reference,Regs_qtd)
        #print(RegRobot)
        for i in range (0,Regs_qtd):
            #print(RegRobot[0])
            try:
                PLC.write_single_register((600+i),int(RegRobot[i]))
                RobotEpson.write_single_register(31+i,RegPLC[i])
                PLC.write_single_register(ConectionAliveReg,0)
                #print(".")
            except Exception as error:
                print(error)
                break
            
StartMainRoutine()       
#--------------------------------------------------------------------------------------------------------------------