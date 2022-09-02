import keyboard
import pyautogui as gui
import time
import random


def get_position():
    on = 0
    box = {}
    while on < 3:
        key = keyboard.is_pressed("ctrl")
        if key == True:
            x, y = (gui.position())
            print(f"X: {x} Y: {y}")
            if not "left" or not "top" in box:
                box["left"] = x
                box["top"] = y
            if on == 2:
                if not "width" or not "height" in box:
                    box["width"] = x - box["left"]
                    box["height"] = y - box["top"]
                    
                elif "left" and "top" and "width" and "height" in box:
                    print(box)
                    break
                else:
                    print(box)
                    break
            time.sleep(0.5)
            on += 1
        else:
            pass
 

    #archive = str(input("Digite o nome que deseja salvar: ")).lower()
    photo = gui.screenshot(region=(box["left"], box["top"], box["width"], box["height"]))
    photo.save(f"screen{random.randint(0, 250)}.png")
    print("\033[01;32mImagem salva com sucesso\033[0m")

get_position()

