
from socket import getaddrinfo, socket
from cv2 import waitKey
from pyModbusTCP.client import ModbusClient
from time import sleep

client01 = ModbusClient(host='192.168.0.30', port=502, auto_open=True, debug=False,unit_id=1)
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

for i in range(0,159):
    try:
        readValue=regs_l = client01.read_input_registers(i, 1)
        print(f"O valor Lido em {i} : {readValue[0]}")

        if((readValue[0])==8302):
            break
          
        
        

    except Exception as ex:
        print(ex)


