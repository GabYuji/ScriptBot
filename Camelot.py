from pyautogui import *
import pyautogui
import time
import random

noCaptcha = True
while noCaptcha:
    locationCaptcha = pyautogui.locateOnScreen("captcha.png", confidence=0.9)
    intervalo = random.randint(1,3)

    if locationCaptcha:
        print("Captcha encontrado")
        noCaptcha = False
        break
    # Encontre a posição da imagem na tela
    locationMessage = pyautogui.locateOnScreen("message.png", confidence=0.8)

    print("Mensagem encontrada: ",locationMessage)
    # Se a imagem for encontrada
    if locationMessage:

        # Clique com o botão esquerdo
        pyautogui.click(locationMessage)

        # Pressione a seta para cima
        pyautogui.press('up')

        # Espere um pouco
        time.sleep(1)

        # Pressione Enter

        pyautogui.press('enter')

        time.sleep(2)

        boss35 = pyautogui.locateOnScreen("boss.png", confidence=0.7)
        if boss35:
            time.sleep(2)
            iconPosition = pyautogui.locateOnScreen("ability.png")
            pyautogui.click(iconPosition)

            time.sleep(2)

            bossAlive = True

            while bossAlive:
                winPosition = pyautogui.locateOnScreen("win.png",confidence=0.6)
                print("Box de vitória: ",winPosition)
                if winPosition:
                    print("Boss Dead")
                    bossAlive = False
                else:
                    print("Boss Alive")
                    iconLocation = pyautogui.locateOnScreen("icon.png")
                    pyautogui.click(iconLocation)
                    time.sleep(1)

    print(intervalo)
    time.sleep(intervalo)
