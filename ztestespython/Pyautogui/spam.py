import pyautogui
import time

time.sleep(2)
b = 1
# if b < 100:
#     pyautogui.write("OI")
#     b = b+1

for b in range (10):
    pyautogui.write("OI")
    pyautogui.press("enter")
    b = b + 1