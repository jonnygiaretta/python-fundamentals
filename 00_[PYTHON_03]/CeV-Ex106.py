def lin(): 
    print('=-='*20)
def ajuda():
    comando = ''
    lin()
    text1 = '>Sistema de Ajuda PyHelp<'
    print(f'\033[1;34m{text1.center(60)}\033[m')
    while True:
        lin()
        comando = str(input('=> Digite Aqui a Função/Biblioteca: ')).strip().lower()
        if comando == 'fim':
            break
        lin()
        print('\033[7;30m', end='')
        print(help(comando))
        print('\033[m', end='')
ajuda()
lin()
text2 = ('Obrigado Por Utilizar o Programa PyHelp!')
text3 = ('Finalizando Programa, Até Logo!')
print(f'\033[1;31m{text2.center(60)}\033[m')
print(f'\033[1;31m{text3.center(60)}\033[m')
lin()