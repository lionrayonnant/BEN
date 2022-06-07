# Bonjour confrères STI2D SIN. Je vous souhaite bien du courage et de l'ambition pour votre projet
# Ce code a été élaboré à partir de la bibliothèque nécessaire aux moteurs, lien Github : https://github.com/DFRobot/DFRobot_RaspberryPi_Motor
# J'ai aussi utilisé la bibliothèque des capteurs ultrason que j'ai ensuite couplés à une bibliothèque qui permet d'utiliser Grove ( arduino ) avec du code python.
# Lien de la bibliothèque Grove vers Python : https://github.com/Seeed-Studio/grove.py
# Le robot s'apelle BEN
# Date : 07/06/2022

from __future__ import print_function
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import sys
import os
sys.path.append("../")

import time

from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board

board = Board(1, 0x10)    # Select bus 1, set address to 0x10

def board_detect():
  l = board.detecte()
  print("Board list conform:")
  print(l)

''' print last operate status, users can use this variable to determine the result of a function call. '''
def print_board_status():
  if board.last_operate_status == board.STA_OK:
    print("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    print("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    print("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    print("board status: parameter error, last operate no effective")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    print("board status: unsupport board framware version")

if __name__ == "__main__":

  board_detect()    # If you forget address you had set, use this to detected them, must have class instance

  # Set board controler address, use it carefully, reboot module to make it effective
  '''
  board.set_addr(0x10)
  if board.last_operate_status != board.STA_OK:
    print("set board address faild")
  else:
    print("set board address success")
  '''
  
  print("Hello STI2D")

  while board.begin() != board.STA_OK:    # Board begin and check board status
    print_board_status()
    print("board begin faild")
    time.sleep(2)
  print("board begin success")

  board.set_encoder_enable(board.ALL)                 # Set selected DC motor encoder enable
  board.set_encoder_reduction_ratio(board.ALL, 43)    # Set selected DC motor encoder reduction ratio, test motor reduction ratio is 43.8

  board.set_moter_pwm_frequency(1000) # Set DC motor pwm frequency to 1000HZ

  sonar1 = GroveUltrasonicRanger(12) # pin12, slot D12
  sonar2 = GroveUltrasonicRanger(16) # pin12, slot D12
  compteur = 0
      
      
  #Début du script de déplacements
  time.sleep(2)    
  while ((sonar1.get_distance() + sonar2.get_distance())/2) > 30 and compteur < 4:  #Cette boucle while fais la moyenne des deux capteurs et tant que cette moyenne est inférieur à 30 ( 30cm ) alors le script s'éxécutes.
   board.motor_movement([board.M1], board.CCW, 95)    # DC motor 1 movement, orientation clockwise
   board.motor_movement([board.M2], board.CW, 95)   # DC motor 2 movement, orientation count-clockwise
   compteur += 1
   time.sleep(1)
   
  compteur = 0
  while ((sonar1.get_distance() + sonar2.get_distance())/2) > 30 and compteur < 1: #Cette boucle while fais la moyenne des deux capteurs et tant que cette moyenne est inférieur à 30 ( 30cm ) alors le script s'éxécutes.
   board.motor_movement([board.M1], board.CCW, 50)    # DC motor 1 movement, orientation clockwise
   board.motor_movement([board.M2], board.CW, 0)   # DC motor 2 movement, orientation count-clockwise
   compteur += 1
   time.sleep(1.2)
   
  compteur = 0
  while ((sonar1.get_distance() + sonar2.get_distance())/2) > 30 and compteur < 10:  #Cette boucle while fais la moyenne des deux capteurs et tant que cette moyenne est inférieur à 30 ( 30cm ) alors le script s'éxécutes.
   board.motor_movement([board.M1], board.CCW, 95)    # DC motor 1 movement, orientation clockwise
   board.motor_movement([board.M2], board.CW, 95)   # DC motor 2 movement, orientation count-clockwise
   compteur += 1
   time.sleep(1)
   
  compteur = 0 
  while ((sonar1.get_distance() + sonar2.get_distance())/2) > 30 and compteur < 1:  #Cette boucle while fais la moyenne des deux capteurs et tant que cette moyenne est inférieur à 30 ( 30cm ) alors le script s'éxécutes.
   board.motor_movement([board.M1], board.CCW, 0)    # DC motor 1 movement, orientation clockwise
   board.motor_movement([board.M2], board.CW, 50)   # DC motor 2 movement, orientation count-clockwise
   compteur += 1
   time.sleep(1.4)
   
  compteur = 0
  while ((sonar1.get_distance() + sonar2.get_distance())/2) > 30 and compteur < 8:  #Cette boucle while fais la moyenne des deux capteurs et tant que cette moyenne est inférieur à 30 ( 30cm ) alors le script s'éxécutes.
   board.motor_movement([board.M1], board.CCW, 95)    # DC motor 1 movement, orientation clockwise
   board.motor_movement([board.M2], board.CW, 95)   # DC motor 2 movement, orientation count-clockwise
   compteur += 1
   time.sleep(1) 
    
  print("stop all motor")
  board.motor_stop(board.ALL)   # stop all DC motor
  print_board_status()
  time.sleep(4) #petite sieste pour le robot
