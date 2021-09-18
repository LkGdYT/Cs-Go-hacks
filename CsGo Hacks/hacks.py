import mouse
import keyboard
from time import sleep

def L():
    keyboard.press_and_release('y')
    sleep(0.1)
    keyboard.write('I just got trolled by a fake hacked client made by Lk_Gd#0848')
    keyboard.press_and_release('enter')

mouse.on_click(L)

keyboard.wait('backspace')