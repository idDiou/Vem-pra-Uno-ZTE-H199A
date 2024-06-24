import pyautogui as pa
import time
import pyperclip
import keyboard
import os
import threading

#intervalo entre os comandos
pa.PAUSE = 1

#Para poder interromper o código
interromper = False
def monitorar_interrupcao():
    global interromper
    keyboard.wait('esc')
    interromper = True
    print("Interrupção solicitada pelo usuário. Finalizando...")

def main():
    global MAC
    print('-----Bem Vindo ao Automatizador VPU-----')
    MAC = input('por gentileza digite o mac: ')
    print('o mac é:', MAC)    
    acesso()

#acessa o navegador
def acesso():
    if interromper:
        return
    pa.press('Win')
    pa.write('edge')
    pa.press('enter')
    RoteadorRua()

#Loga no roteador
def RoteadorRua():
    if interromper:
        return
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('Vpu@2018')
    pa.press('enter')
    wan()

#acessa a Wan e altera o ppoe
def wan():
    if interromper:
        return
    pa.press('tab', 3)
    pa.press('enter')
    pa.press('tab', 7)
    pa.press('enter')
    pa.press('f11')
    pa.click(x=659, y=488)
    pa.press('tab', 8)
    pa.write(MAC[-6:] + '@vemprauno')
    lan()

#acessa o wifi e senha
def lan():
    if interromper:
        return
    pa.press('tab', 11)
    pa.press('enter')
    pa.press('home')
    pa.press('tab', 9)
    pa.press('enter')
    pa.press('tab', 7)
    pa.press('enter')
    pa.click(x=724, y=969)
    pa.press('tab', 3)
    g4()

#usuario e senha do 4g
def g4():
    pa.write('VempraUno_' + MAC[-4:])
    pa.press('tab', 3)
    pa.write(MAC[-8:])
    pa.press('tab', 4)
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')
    

if __name__ == "__main__":
    # Inicia o monitoramento da tecla de interrupção em uma thread separada
    interrupcao_thread = threading.Thread(target=monitorar_interrupcao)
    interrupcao_thread.daemon = True
    interrupcao_thread.start()
    
    main()