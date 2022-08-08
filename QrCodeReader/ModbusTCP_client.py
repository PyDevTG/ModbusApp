#---------Modbus-----------------------------------------------------------------------
from pyModbusTCP.client import ModbusClient
from time import sleep
#---------Area de configuração Modbus

client01 = ModbusClient(host='192.168.0.10', port=502, auto_open=True, debug=False)
try: 
    
    client01.open()
except Exception as Ex:
    print(Ex)

if(client01.open()):
    print("=============================")
    print("Cliente Connectado ao PLC")
    print("=============================")
else:
    client01.close()
    print("=============================")
    print("Cliente Não Conectado ao PLC !!!")
    print("=============================")

"""Registradores"""
reg_command = 1020 #D1020
regs_Data1 = 1021 # D1021
regs_Data2 = None
"""-------------"""
Comando =None
#--------------------------------------------------
def OpenModbus():
    client01.open()
    if(client01.open()):
        print("=============================")
        print("Cliente Connectado ao PLC")
        print("=============================")
        
#---------------------------------------
def FecharModbus():
    client01.close()
    print("=============================")
    print("Cliente Modbus Desconectado ")
    print("=============================")

############################################################################################################################
def ReadRegister(reg):
    registrador = reg
    if(client01.open()):
        Comando = client01.read_holding_registers(registrador, 1)
        return Comando[0]
        
    else:
        Comando = 0
        print("Cliente Modbus não Conectado")
        OpenModbus()
        print("Abrindo Conexão")
    
    

############################################################################################################################
def WriteReg(reg,value):
    registrador = reg
    valor = value
    if(client01.open()):
        client01.write_single_register(registrador,value)#Envia Resposta no mesmo registrador com o valor 01
        Comando=0
