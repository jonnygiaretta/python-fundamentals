from time import sleep
from arquivos import lerarquivo, cadastrar
def lin():
    print('=-='*15)

def menu():
    lin()
    print('Menu Principal'.center(45))
    lin()
    print('1 - Ver Pessoas Cadastradas')
    print('2 - Cadastrar Uma Nova Pessoa')
    print('3 - Sair do Sistema')
    lin()
        
def valid(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError,TypeError):
            print('Erro: Por Favor Digite um Valor Inteiro Valido')
            lin()
        else: 
            if n in [1, 2, 3]:
                return n        
            else:
                print('Erro: Digite uma Opcao Valida do Menu')
                lin()
                
def opt(n, arq):
    """
    Controla o Direcionamento do Menu.
    Retorna True se o Sistema deve continuar ou False se deve parar
    """
    lin()
    if n == 1:
        print('Opção 1 Selecionada: Ver Pessoas Cadastradas.'.center(45))
        lin()
        lerarquivo(arq)
    elif n == 2:
        print('Opção 2 Selecionada: Cadastrar uma Nova Pessoa'.center(45))
        lin()
        nome = str(input('Nome: ')).strip()
        while True:
            try:
                idade = int(input('Idade: '))
            except (ValueError, TypeError):
                print('Erro: Digite uma idade válida (número inteiro).')
            else:
                break
        cadastrar(arq, nome, idade)
    elif n == 3:
        print('Finalizando Sistema... , Até Logo!'.center(45))
        return False
    lin()
    sleep(1.5)
    return True
