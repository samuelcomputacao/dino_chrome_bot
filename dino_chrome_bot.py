
import time

import pyscreenshot as ImageGrab
import pyautogui

investiu = False
investimentos = 1

# Take screenshot using PIL lib
def capture_screen():
    screen = ImageGrab.grab()
    return screen

# Detects enemy by diff in pixel color in region of detections
def detect_down(screen):
   # aux_color = screen.getpixel((1013,821))
    aux_color = screen.getpixel((677,644))
    return aux_color[0] > 130
def detect_up(screen):
    aux_color = screen.getpixel((677,698))
    return aux_color[0] > 130
    
def clickDown():
    pyautogui.moveTo(1267, 592, 1)
    pyautogui.click()
    relatorio()

def clickUp():
    pyautogui.moveTo(1267, 528, 1)
    pyautogui.click()
    relatorio()

def relatorio():
    print("--------------------")
    print("Ivestimentos: %s" % investimentos)
    print("-------------------\n\n")

def clickReload():
    pyautogui.moveTo(86, 80, 1)
    pyautogui.click()
    print("reload")

timeInicio = 0
timeAux = 0
timeReload = time.time()
while True:
    screen = capture_screen()
    if not investiu:
        if detect_down(screen) :
            print("cima")
            if(timeAux==0):
                timeAux = time.time()

            if((time.time() - timeAux) > 1):
                clickDown()
                invertiu = True
                timeInicio = time.time()
                investimentos += 1
                timeAux = 0
            
        elif detect_up(screen):
            print("baixo")
            if(timeAux==0):
                timeAux = time.time()

            if((time.time() - timeAux) > 1):
                clickUp()
                timeInicio = time.time()
                invertiu = True
                investimentos += 1
                timeAux=0
        else:
           timeAux=0
    else:
        if (time.time()-timeInicio) > 5 :
            investiu = False
            timeInicio = time.time()
    
    if((time.time() - timeReload) > 100):
        clickReload()
        timeReload = time.time()