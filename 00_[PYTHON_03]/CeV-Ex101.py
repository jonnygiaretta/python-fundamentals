from datetime import date
anoatual = date.today().year

def lin():
    print('=-='*20)

lin()

def voto(): 
    lin()
    v = anoatual - ano
    if v >= 65 : 
        return f'Voce Nasceu em {ano}, Portanto Tem {v} Anos & o Voto é OPCIONAl No Seu Caso'
    elif v >= 16:
        return f'Voce Nasceu em {ano}, Portanto Tem {v} Anos & o Voto é OBRIGATORIO No Seu Caso'
    elif v < 16 : 
        return f'Voce Nasceu em {ano}, Portanto Tem {v} Anos & o Voto é RESTRITO No Seu Caso'
    
ano = int(input('Em Qual Ano Voce Nasceu : '))
print(voto())
lin()