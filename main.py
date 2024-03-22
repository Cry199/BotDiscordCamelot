import cv2
import numpy as np
import pyautogui
import keyboard
import time
import sys

screen = 0
screenshot_gray = 0
max_val = 0
max_loc = 0

imagemDeEscolha = ""

imagens = {
    "espada": cv2.imread("img\\espada.png", 0),
    "pular": cv2.imread("img\\ignorarmensagem.png", 0),
    "won": cv2.imread("img\\won.png", 0),
    "lost": cv2.imread("img\\lost.png", 0)
}

def screenshot():
    capturarTela()
    processarTela()

def capturarTela():
    global screen
    screen = pyautogui.screenshot()

def processarTela():
    global screen
    global screenshot_gray

    screenshot = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

def procurarImagem(imagem):
    global screenshot_gray
    global max_val
    global max_loc

    resultado = cv2.matchTemplate(screenshot_gray, imagem, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

def colocarDungeon():
    global max_val
    global max_loc

    if max_val > 0.8:
        pyautogui.moveTo(max_loc)
        pyautogui.click()
        time.sleep(3)
        keyboard.write('/')
        keyboard.write('dungeon difficulty:difficult')
        keyboard.press('enter')
        time.sleep(1.5)

while True:
    time.sleep(1.5)

    screenshot()

    imagemDeEscolha = imagens["pular"]
    procurarImagem(imagemDeEscolha)

    if max_val > 0.8:
        time.sleep(1)
        pyautogui.moveTo(max_loc)
        pyautogui.click()
        continue

    time.sleep(1.5)
    imagemDeEscolha = imagens["won"]
    procurarImagem(imagemDeEscolha)
    colocarDungeon()

    time.sleep(1.5)
    imagemDeEscolha = imagens["lost"]
    procurarImagem(imagemDeEscolha)
    colocarDungeon()

    imagemDeEscolha = imagens["espada"]
    procurarImagem(imagemDeEscolha)

    if max_val > 0.8:
        pyautogui.moveTo(max_loc)
        pyautogui.click()