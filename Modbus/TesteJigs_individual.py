

from pyModbusTCP.client import ModbusClient
from time import sleep

client01 = ModbusClient(host='192.168.0.10', port=502, auto_open=True, debug=False)
client01.open()
if(client01.open()):
    print("=============================")
    print("Cliente Connectado ao PLC")
    print("=============================")
    print("=============================")
"""Registradores"""
regs_l = None 
regs_2 = None
reg=200
"""-------------"""

JIG=int(input(" QUAL JIG DESEJA TESTAR ?: "))

if(JIG==1):
    reg=200
elif(JIG==2):
    reg=300
elif(JIG==3):
    reg=400
elif(JIG==4):
    reg=500
else:
    print("error")


Tarefa =input(" Start automatic JIG 01 TEST - Digite 1 // Para zerar Digite 0 : ")  

if(int(Tarefa))==1:
    print("Iniciando Testes")
    print("Inserir Card")
    client01.write_single_register(reg,2)
    sleep(5)
    print("Retirar Card")
    client01.write_single_register(reg,4)
    sleep(5)
    print("Iniciar Teste de Teclado")
    client01.write_single_register(reg,5)
    sleep(10)
    regs_l = client01.read_holding_registers(reg, 1)
    
    if int(regs_l[0]) == 6 :
        print("Teste de Teclado Finalizado")

        client01.write_single_register(reg,7)
        print("Iniciando Teste de Som")
    sleep(5)    
    client01.write_single_register(reg,9)
    print("Teste de Som Finalizado")
    sleep(5)
    regs_2 = client01.read_holding_registers(reg, 1)
    if int(regs_2[0]) == 10 :
        client01.write_single_register(reg,12)
        print("Produto Reprovado - Default")
        print("Teste Automatizado Finalizado")
        client01.close()
else:
    Tarefa = 0
    client01.write_single_register(reg,12)
    print("Teste Não Iniciado")
    client01.close()




