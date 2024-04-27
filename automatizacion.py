import keyboard
import pyautogui as pa
import random
import time

#Programa nomas pa ganar el logro Bublle People

#Aqui decides cuantos movimientos hara antes de cada reinicio
clicks_left = 5


while clicks_left > 0:
# Genera una posición aleatoria dentro de un rango
#ESTE ES EL RANGO QUE LE TIENES QUE DAR:
    x_random = random.randint(650, 1200)
    y_random = random.randint(380, 650)

    if clicks_left == 1:
#ESTE ES LA UBICACION DEL BOTON:
        pa.click(x=968, y=843, duration=1)  # Hace clic y mantiene pulsado durante 1 segundo
        clicks_left = 7
        if keyboard.is_pressed('q'):
            print ('q clickeada')
            break

#esta parte es la que mueve aleatoriamente  
    pa.dragTo(x_random, y_random, duration=1)  # Mueve el cursor a la posición aleatoria
    clicks_left -= 1
    pa.mouseUp()
    time.sleep(0.2)

  #Si quieres apagar el programa solo mantiene presionada la letra "q"
    if keyboard.is_pressed('q'):
        print ('q clickeada')
        break
