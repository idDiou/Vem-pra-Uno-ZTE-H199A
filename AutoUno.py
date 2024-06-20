import pyautogui as pa
import time
import pyperclip

print ('ola minion')
#intervalo entre os comandos
pa.PAUSE = 1

#acessa o navegador
pa.press('Win')
pa.write('edge')
pa.press('enter')

#acessa o roteador
pa.write('192.168.1.1')
pa.press('enter')
pa.write('multipro')
pa.press('tab')
pa.write('multipro')

#acessa o gerenciamento 
pa.press('enter')
pa.hold('win')
pa.press('up')
pa.press('tab', 5)
pa.press('enter')
pa.press('tab', 9)
pa.press('enter')
pa.press('F11')
pa.click(x=1624, y=222)
pa.mouseDown(button='left')
time.sleep(1)
pa.mouseUp(button='left')
pa.click(x=1531, y=223)

#acessa o backup
pa.click(x=663, y=696)
pa.press('tab')
pa.press('enter')
pa.press('tab', 6)
pa.press('enter')
pa.write('C:\\Users\\diona\\AppData\\Local\\Programs\\Python\\Python311\\Projetos\\Automatizar H199A')
pa.press('enter')
pa.press('tab', 6)
pa.write('defaut')
pa.press('enter')

#confirma o backup
pa.press('tab')
pa.press('enter')
pa.press('tab')
pa.press('enter')



