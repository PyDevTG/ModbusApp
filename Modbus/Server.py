from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
import random

class ServidorModbusTCP():

    def __init__(self, Host_ip,Port ):
        self._server = ModbusServer(host=Host_ip, port=Port, no_block=True)
        self._db = DataBank
        self._state =[0]
    def Run(self):
        
        try:
            self._server.start()
            print("The server has Started")
        except Exception as x:
            self._server.stop()
            print(x.args)
            

        while True:

            if(self._server.is_run==True): 
           
                self._db.set_words(0,[5])
                self._state=self._db.get_words(1)
                print(f"Get BIT 2:{self._state}")
                sleep(1)
                

    

    