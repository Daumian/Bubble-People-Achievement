import keyboard
import pyautogui as pa
import random
import time

#CUADRANGULAR
e_pressed = False
while True:
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('e') and not e_pressed:
        print(pa.position())
        e_pressed = True
    elif not keyboard.is_pressed('e'):
        e_pressed = False
