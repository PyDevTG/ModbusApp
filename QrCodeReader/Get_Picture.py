################################################################################################################
################################################################################################################
###### This Code is to detect a QRCODE or Barcode 
###### Autor: Eng. Thiago Alves
###### This Code is using Modbus TCP Client to get the picture from camera and save on local folder
###### #########################################################################################################



#Import the libraries
from cv2 import CAP_PROP_AUTOFOCUS
from pyzbar import pyzbar
import cv2
from cv2 import CAP_PROP_EXPOSURE
from cv2 import CAP_PROP_BACKLIGHT
from cv2 import CAP_PROP_SATURATION
from cv2 import cvtColor
from cv2 import CAP_PROP_BRIGHTNESS
from cv2 import CAP_PROP_FPS
import numpy as np
import ModbusTCP_client as mb

#----criação do Objeto
CamNumber = 0
#-----------Função de captura de imagem----------------------------------------------------
def getpicture(var):
    print("Iniciando Camera ...")
    
    
    img, frame = var.read()
     #--------Redimensiona Imagem-------------
    scale = 1.5
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    frame = cv2.resize(frame, (width, height))
        #-----------------#--------------------#
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #gray_flip=cv2.flip(gray,1)
    #img_not = cv2.bitwise_not(gray)
    imageReady=gray

    #cv2.imshow("image", imageReady)
    cv2.imwrite('QrcodeImage.png', imageReady)
    #var.release()
    #cv2.destroyAllWindows()
#----------Função de Video Stream----------------

#########################################################################################################################

def VideoStream():
    #Start PROGRAM
    print("Iniciando QRCODE Reader")
    cam = cv2.VideoCapture(CamNumber)
    CamParameters(cam)
    print("Fazendo Varreduras")
    barcodes = None 
    qrCodeDetector = cv2.QRCodeDetector()
    
 
    while True:
        img, frame = cam.read() # captura de imagem

        #--------Redimensiona Imagem-------------
        scale = 1.5
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        frame = cv2.resize(frame, (width, height))
        #-----------------#--------------------#

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #gray_flip=cv2.flip(gray,1)
        img_not = cv2.bitwise_not(gray)
        ImgREADY = gray

        #----------Decodificar a Imagem em tempo real------LIB01------------
        barcodes = pyzbar.decode(ImgREADY)
        if(barcodes != []):
            for barcode in barcodes:
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                (x, y, w, h) = barcode.rect
                text = "{}".format(barcodeData)
                cv2.rectangle(ImgREADY, (x, y), (x + w, y + h), (255, 10, 255), 2)
                cv2.putText(ImgREADY, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)  
                
                #print(text)
##########################################################################################################################        
#---------------------------------------------------------------------------

        cv2.imshow("Frame",ImgREADY) # mostra a imagem
                    
        if not img:
            print("failed to grab frame")
            break
               
        k = cv2.waitKey(1)
        #-------------Espera comando do PLC para capturar Imagem
        modbusValue=mb.ReadRegister(1020)
        
        if(modbusValue==2):
            mb.WriteReg(1020,1)
            getpicture(cam)#Captura Imagem da Camera
            print("Imagem Capturada")
            readImage()#Processa imagem e procura por codigo

        #----------------------------------------------------------
      
        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        if k == 13:
            # ENTER pressed captura a imagem e processa
            getpicture(cam)
            readImage()
            print("Imagem Capturada")
    

    cam.release()

    cv2.destroyAllWindows()
############################################################################################################################
#---------------------------------------------------------
def readImage():

    print("Iniciando Leitura de imagem ...")
    #Ler imagem armazenada da pasta local
    imagem = cv2.imread("QrcodeImage.png")
    #scale = 0.3
    #width = int(imagem.shape[1] * scale)
    #height = int(imagem.shape[0] * scale)
    #imagem = cv2.resize(imagem, (width, height))
    barcodes = None # inicia variavel barcodes com NONE
    barcodes = pyzbar.decode(imagem) #Decodifica imagem
    
    #-------Rotina de Decodificação, Marcação do codigo lido e Impressão dos dados
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        (x, y, w, h) = barcode.rect
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 20, 255), 2)
        text = "{}".format(barcodeData)
        print(text)#Print da informação Contida no QRCODE
        cv2.putText(imagem, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        mb.WriteReg(1021,1)
        mb.WriteReg(40032,8)#NOk codigo não encontrado
        mb.WriteReg(30032,15)
        print(mb.ReadRegister(30032))#NOk codigo não encontrado
        #print(mb.ReadRegister(40032))#NOk codigo não encontrado
    #----Caso não tenha encontrado o QRCOde ou Codigo de barras
    if(barcodes==[]):
        print("Não foi encontrado nenhum código na imagem!")
        
        mb.WriteReg(1021,0)#NOk codigo não encontrado
        



   

    """while True:
        cv2.imshow("Original", imagem)
        key = cv2.waitKey(1) 
        if key == 27:
            break
"""

##############################################################################################################################

#------------Função de configurações da camera ------------
def CamParameters(var_cam):
    var_cam.set(CAP_PROP_EXPOSURE,-7.0)
    var_cam.set(CAP_PROP_BRIGHTNESS,-100)
    var_cam.set(CAP_PROP_FPS,0)
    var_cam.set(CAP_PROP_SATURATION,-200)
    var_cam.set(CAP_PROP_AUTOFOCUS,10)



#----------------------------main Execution ------------------------------------------

