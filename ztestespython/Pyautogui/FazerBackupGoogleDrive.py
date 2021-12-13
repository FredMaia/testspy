import pyautogui
import time

pyautogui.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
pyautogui.PAUSE = 0.5 #cada comando é executado a cada meio segundo

# Abrir o Google Drive no computador
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
#time.sleep(1)
# pyautogui.write('https://drive.google.com')
pyautogui.press('enter')

# Entrar na área de trabalho
pyautogui.hotkey('winleft','d')

# Clicar no arquivo e arrastar
pyautogui.moveTo(567,38) #Passar o x, depois o y da função position()
pyautogui.mouseDown()
pyautogui.moveTo(756,635)

# Enquanto estiver arrastando mudar para a página do Google Drive
pyautogui.hotkey('alt','tab')

# Soltar o arquivo dentro do Google Drive
pyautogui.mouseUp()

# Esperar alguns segundos
time.sleep(5)
