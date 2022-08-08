from PyQt6 import *
from PyQt6 import QtWidgets
from PyQt6 import uic
import cv2

cam=cv2.VideoCapture(0)
while True:
    img, frame = cam.read()

    #cv2.imshow("Frame",frame)
    k = cv2.waitKey(1)

    if k == 13:
        break

app=QtWidgets.QApplication([])

VideoStream=uic.loadUi("Main.ui")
#QrcodeTela.btnPolRect.clicked.connect()
#QrcodeTela.btnRectPol.clicked.connect()
#QrcodeTela.actionSalva.triggered.connect(salvar)
VideoStream.Image.setText(cv2.imshow("Frame",frame))
VideoStream.show()
app.exec()