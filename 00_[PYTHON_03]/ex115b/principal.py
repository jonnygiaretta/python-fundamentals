from funcoes import lin, menu, valid, opt   
from arquivos import arquivoexiste, criararquivo, lerarquivo
from time import sleep

arq = 'pessoascadastradas.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
while True: 
    menu()            
    n = valid('-> Sua Opção: ')
    sleep(1)
    lin()
    print(f'Verificação Completa, Opção Escolhida: {n}')
    if not opt(n, arq):
        break