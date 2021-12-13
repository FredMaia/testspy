from typing import Text
import pyautogui
import time

pyautogui.PAUSE = 0.1

b = 5

time.sleep(5)

for x in range(200):
    pyautogui.press("enter")
    pyautogui.write("pyautogui.press('enter')")
    pyautogui.press("down")
    pyautogui.press("end")
    b = b + 1
