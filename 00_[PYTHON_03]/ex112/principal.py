from utilidadescev.funcoes.funcoes import aumentar, diminuir, dobro, metade, lin, moeda, resumo
from utilidadescev.dados.dados import leiadinheiro


lin()
res = str(input('Deseja Que as Unidades Monetarias Sejam Formatadas[S/N]: ')).strip().upper()[0]
if res == 'S':
    res = True
    cambio = str(input('Deseja Fazer o Cambio em Qual Moeda[U.M]: '))
elif res == 'N':
    res = False
    cambio = ''
else:
    while True:
        print('Resposta Inválida, Digite Novamente Por Favor.')
        lin()
        res = str(input('Deseja as Unidades Monetarias Formatadas[S/N]: ')).strip().upper()[0]
        if res == 'S':
            res = True
            cambio = str(input('Deseja Fazer o Cambio em Qual Moeda[U.M//Padrão = R$]: '))
            break
        if res == 'N':
            res = False
            cambio = ''
            break    

lin()
p = leiadinheiro('Digite o Valor do Produto: ')
id = float(input('Deseja Que o Desconto Seja de Quanto[%]: '))
ia = float(input('Deseja Que o Aumento Seja de Quantos[%]: '))
lin()
resumo(p, ia, id, cambio, res)
lin()