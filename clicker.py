import pyautogui
import keyboard
import sys

print('Clique "Esc" para cancelar, "shift+1" para iniciar, e "shift+2" para mudar de tecla.')
key = input('Digite as teclas que deseja repetir do contráio será o botão esquerdo do mouse: ')

def clicker():
    while True:
        if key == '':
            pyautogui.click()
        else:
            for c in range(len(key)):
                pyautogui.press(key[c])
        if keyboard.is_pressed('esc'):
            break
def change_key():
    global key
    key = input('Digite a nova tecla ou deixe em branco caso queira o botão esquerdo do mouse: ')


keyboard.add_hotkey("shift+1", clicker)
keyboard.add_hotkey("shift+2", change_key)
keyboard.wait()