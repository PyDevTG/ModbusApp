

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
regs_200=None
regs_300=None
regs_400=None
regs_500=None


"""-------------"""


Tarefa =input(" Start automatic JIGS TEST - Digite 1 // Para zerar Digite 0 : ")  

if(int(Tarefa))==1:
    print("Iniciando Testes")
    print("Inserir Card")
    client01.write_single_register(200,2)
    client01.write_single_register(300,2)
    client01.write_single_register(400,2)
    client01.write_single_register(500,2)
    sleep(5)
    print("Retirar Card")
    client01.write_single_register(200,4)
    client01.write_single_register(300,4)
    client01.write_single_register(400,4)
    client01.write_single_register(500,4)
    sleep(5)
    print("Iniciar Teste de Teclado")
    client01.write_single_register(200,5)
    client01.write_single_register(300,5)
    client01.write_single_register(400,5)
    client01.write_single_register(500,5)
    sleep(10)
    regs_200 = client01.read_holding_registers(200, 1)
    regs_300 = client01.read_holding_registers(300, 1)
    regs_400 = client01.read_holding_registers(400, 1)
    regs_500 = client01.read_holding_registers(500, 1)
    
    if int(regs_200[0]) == 6 :
        print("Teste de Teclado Finalizado")
        client01.write_single_register(200,7)
        print("Iniciando Teste de Som")
    if int(regs_300[0]) == 6 :
        print("Teste de Teclado Finalizado")
        client01.write_single_register(300,7)
        print("Iniciando Teste de Som")
    if int(regs_400[0]) == 6 :
        print("Teste de Teclado Finalizado")
        client01.write_single_register(400,7)
        print("Iniciando Teste de Som")
    if int(regs_500[0]) == 6 :
        print("Teste de Teclado Finalizado")
        client01.write_single_register(500,7)
        print("Iniciando Teste de Som")

    sleep(5)    
    client01.write_single_register(200,9)
    client01.write_single_register(300,9)
    client01.write_single_register(400,9)
    client01.write_single_register(500,9)
    print("Teste de Som Finalizado")
    sleep(5)
    client01.write_single_register(200,12)
    client01.write_single_register(300,12)
    client01.write_single_register(400,12)
    client01.write_single_register(500,12)
    print("Produto Reprovado - Default")
    print("Teste Automatizado Finalizado")
    client01.close()
else:
    Tarefa = 0
    client01.write_single_register(200,12)
    client01.write_single_register(300,12)
    client01.write_single_register(400,12)
    client01.write_single_register(500,12)
    print("Teste Não Iniciado")
    client01.close()




