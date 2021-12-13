import pyautogui
import time


# for i in range(10):
# 	print(' ' * (10-i), "#" * (2*i+1))

# time.sleep(3)


# n = 1

# for i in range(1,n+1):
# 	for j in range(1,i+1):
#  		print(j, end=" ")
# 	print("")

# for i in range(n-1,0,-1):
# 	for j in range(1,i+1):
#  		print(j, end=" ")
# 	print("") 

a = 2
b = 1

pyautogui.PAUSE = 0.5

pyautogui.press("winleft")
pyautogui.write("bloco de notas")
time.sleep(1)
pyautogui.press("enter")

while a < 10:
	pyautogui.write(b)
	pyautogui.press("enter")
	b = b + 1