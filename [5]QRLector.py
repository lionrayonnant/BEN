class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import cv2
import numpy as np
import pyzbar.pyzbar as qr
import json
from tkinter import END
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

with open("data.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

qrdata = jsonObject['cdc']

while True:

    ret,cuadro = cap.read()
    qrdetectado = qr.decode(cuadro)
    data = qrdata

    if(qrdetectado is not None):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)

        for i in qrdetectado:
            qrdatascan = i.data
            if (qrdata)==(str((qrdatascan).decode("utf-8"))):
                cv2.rectangle(cuadro,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,255,0),3)
                cv2.putText(cuadro,str((qrdatascan).decode("utf-8")),(30,30),font,1,(0,255,0),2)
                GPIO.output(12, GPIO.HIGH)

            else:
                cv2.rectangle(cuadro,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,0,255),3)
                cv2.putText(cuadro,str((qrdatascan).decode("utf-8")),(30,30),font,1,(0,0,255),2)
                GPIO.output(16, GPIO.HIGH)

            
            #if str((qrdatascan).decode("utf-8")):
                #if (qrdata)==(str((qrdatascan).decode("utf-8"))):
                    #print("yes")

    cv2.imshow("Lector QR", cuadro)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        
    

