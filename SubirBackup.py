import pyautogui as pa
import time
import pyperclip
import keyboard
import os

#intervalo entre os comandos
pa.PAUSE = 1

#função principal/inicial
def main():
    print('-----Bem Vindo ao Automatizador VPU-----')
    MAC = input('por gentileza digite o mac: ')
    print('o mac é:', MAC)
    verificar()

#Verificação
def verificar():
    while True:
        print('1-Roteador Novo da Caixa')
        print('2-Roteador da Rua')
        try:
            veri = int(input('digite uma opção: '))
            if veri == 1:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorF()
                novo()
                gerenciamento()
                backup()
                Cbackup()
                break
            
            elif veri == 2:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorRua()
                gerenciamento()
                backup()
                Cbackup()
                break
            
            else:
                print ('opção inválida')
            
        except ValueError: 
            os.system('cls')
            print('Entrada inválida. Digite apenas números.')
            print('digite enter para continuar')
            keyboard.wait('any')


#acessa o navegador
def Acesso():
    pa.press('Win')
    pa.write('edge')
    pa.press('enter')

#acessa o roteador caso seja de fábrica
def RoteadorF():    
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('multipro')
    pa.press('enter')

def RoteadorRua():
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('Vpu@2018')
    pa.press('enter')

#remove o assistente
def novo():
    pa.press('tab', 6)
    pa.press('enter')

#acessa o gerenciamento 
def gerenciamento():
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
def backup():
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
def Cbackup():
    pa.press('tab')
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')

if __name__ == "__main__":
    main()

