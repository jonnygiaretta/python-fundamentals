from funcoes import lin, menu, valid, opt    
from time import sleep  

while True: 
    menu()            
    n = valid('-> Sua Opção: ')
    sleep(1)
    lin()
    print(f'Verificação Completa, Opção Escolhida: {n}')
    if not opt(n):
        break
