
from socket import getaddrinfo, socket
from pyModbusTCP.client import ModbusClient
from time import sleep
import os

client01 = ModbusClient(host='192.168.0.10', port=502, auto_open=True, debug=False,unit_id=1)
try:
    client01.open()
    
   
    
    if(client01.open()):
        print("=============================")
        print("Cliente Connectado ao PLC")
        print("=============================")
        print("=============================")
    else:
        print("Não foi possivel conectar ao Host")

except Exception as Ex:
    print(Ex)
    print("Não foi possivel conectar ao Host")


"""Registradores"""
regs_l=None
while (True and client01.open()):
    print("========================================================================")
    Resp=input("Qual é o Registrador de Referencia ? ")

    registrador = int(Resp)

    operacao=input("Deseja Ler (1) ou Escrever (2) ?")
    print("========================================================================")
    print("========================================================================")

    if(int(operacao)==1):
        if(client01.open()):
            try:
                readValue=regs_l = client01.read_holding_registers(registrador, 1)
                print(f"O valor Lido : {readValue[0]}")
            except Exception as ex:
                print(ex)

        
    elif(int(operacao)==2):
        value=input("Digite o valor que deseja escrever: ")
        if(client01.open()):
            try:
                client01.write_single_register(registrador,int(value))
                #client01.write_single_coil(registrador,False)
                print(f"Valor {value} escrito no registrador : {registrador}")
                
            except Exception as ex:
                print(ex)

        
    else:
        print("Valor invalido")  
    print("========================================================================")
    Continue=input("Deseja Continuar? [1]Sim [2]Não :")
    print("========================================================================")
    if(int(Continue) == 2):
        break
    else:
        os.system('cls')

