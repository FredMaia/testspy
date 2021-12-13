import pyautogui
import time

pyautogui.alert("O código irá começar. Tire a mão do teclado e do mouse")
pyautogui.PAUSE = 0.5 #cada comando é executado a cada meio segundo


pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('meet.google.com/gpa-zgem-qpj')
pyautogui.press('space')
time.sleep(2)
pyautogui.press('enter')

#Desligar câmera e microfone
time.sleep(5)
pyautogui.hotkey('ctrlleft','e')
pyautogui.hotkey('ctrlleft','d')

#Trocar de conta
pyautogui.moveTo(x=1260, y=113)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(658, 331)
pyautogui.click()

#Desligar câmera e microfone
time.sleep(5)
pyautogui.hotkey('ctrlleft','e')
pyautogui.hotkey('ctrlleft','d')
time.sleep(3)

#Entrar na sala
pyautogui.moveTo(x=964, y=424)
pyautogui.click()

# # Esperar alguns segundos
time.sleep(2)

pyautogui.alert("O código terminou de ser executado.")