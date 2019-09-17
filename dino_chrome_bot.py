
import time

import pyscreenshot as ImageGrab
import pyautogui


# Region of detections
# Coordenates for resolution 1600x900
X = 655.0  # X2 = X + 15
Y1 = 215
Y2 = 250


# Take screenshot using PIL lib
def capture_screen():
    screen = ImageGrab.grab()
    return screen


# Detects enemy by diff in pixel color in region of detections
def detect_down(screen):
   # aux_color = screen.getpixel((1013,821))
    aux_color = screen.getpixel((2523,825))
    return aux_color[0] > 130
def detect_up(screen):
    aux_color = screen.getpixel((2523,915))
    return aux_color[0] > 130


# Dino Jumps
def jump():
    global X
    pyautogui.press("up")
    X += 0.4  # Increment in detection region for increase speed of game
def clickDown():
    pyautogui.moveTo(3101, 592, 1)
    pyautogui.click()
def clickUp():
    pyautogui.moveTo(3101, 528, 1)
    pyautogui.click()

print("Start in 3 seconds...")
time.sleep(3)

# Infinite Loop of bot
investiu = False;
cont = 0
contInvestido = 0
investimentos = 0
while True:

    print("-------------------")
    print("Tempo sem investir %i" % contInvestido)
    print("Fora da média: %i" % cont)
    print("Investiu: %s" %(investiu))
    print("Ivestimentos: %s" % investimentos)
    print("-------------------\n\n")
    screen = capture_screen()
    if not investiu:
        if detect_down(screen) :
            cont += 1
            if(cont > 20):
                clickDown()
                invertiu = True
                contInvestido = 0
                investimentos += 1
            
        elif detect_up(screen):
            cont += 1
            if(cont > 20):
                clickUp()
                invertiu = True
                contInvestido = 0
                investimentos += 1
        else:
            cont = 0
    else:
        if contInvestido > 60:
            investiu = False
            contInvestido = 0
        else:
            contInvestido += 1