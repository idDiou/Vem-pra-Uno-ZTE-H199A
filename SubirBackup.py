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

#função principal/inicial
def main():
    print('-----Bem Vindo ao Automatizador VPU-----')
    MAC = input('por gentileza digite o mac: ')
    print('o mac é:', MAC)
    verificar()

#Verificação
def verificar():
    while not interromper:
        print('1-Roteador Novo da Caixa')
        print('2-Roteador da Rua')
        try:
            veri = int(input('digite uma opção: '))
            if veri == 1:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorF()
                break
            
            elif veri == 2:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorRua()
                break
            
            else:
                print ('opção inválida')
            
        except ValueError: 
            os.system('cls')
            print('Entrada inválida. Digite apenas números.')
            print('digite enter para continuar')
            keyboard.wait('enter')
        if interromper:
            break

#acessa o navegador
def Acesso():
    if interromper:
        return
    pa.press('Win')
    pa.write('edge')
    pa.press('enter')

#acessa o roteador caso seja de fábrica
def RoteadorF():  
    if interromper:
        return  
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('multipro')
    pa.press('enter')
    novo()

def RoteadorRua():
    if interromper:
        return
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('Vpu@2018')
    pa.press('enter')
    gerenciamento()

#remove o assistente
def novo():
    if interromper:
        return
    pa.press('tab', 6)
    pa.press('enter')
    gerenciamento()

#acessa o gerenciamento 
def gerenciamento():
    if interromper:
        return
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
    backup()

#acessa o backup
def backup():
    if interromper:
        return
    pa.click(x=663, y=696)
    pa.press('tab')
    pa.press('enter')
    pa.press('tab', 6)
    pa.press('enter')
    pa.write('C:\\Users\\diona\\AppData\\Local\\Programs\\Python\\Python311\\Projetos\\Automatizar H199A')
    pa.press('enter')
    pa.press('tab', 6)
    pa.write('default')
    pa.press('enter')
    Cbackup()

#confirma o backup
def Cbackup():
    if interromper:
        return
    pa.press('tab')
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')

if __name__ == "__main__":
    # Inicia o monitoramento da tecla de interrupção em uma thread separada
    interrupcao_thread = threading.Thread(target=monitorar_interrupcao)
    interrupcao_thread.daemon = True
    interrupcao_thread.start()
    
    main()