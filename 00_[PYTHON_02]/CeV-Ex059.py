
opcao = 0
n1 = int(input('Primeiro Valor : '))
n2 = int(input('Segundo Valor : '))

while opcao != 5 :
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Numeros')
    print('[ 5 ] Sair do Programa')
    opcao = int(input('>>> Qual a Sua Opção : '))

    if opcao == 1 : 
        print(f'A Soma Entre ({n1} + {n2}) = ({n1 + n2})')
        print('=-='*10)
    
    elif opcao == 2 : 
        print(f'A Multiplicação Entre ({n1} + {n2}) = ({n1 * n2})')
        print('=-='*10)
    
    elif opcao == 3 : 
        if n1 > n2 :
            maior = n1
        else : 
            maior = n2
        print(f' Entre {n1} & {n2} O Maior Valor : {maior}')
        print('=-='*10)

    elif opcao == 4 : 
        print('Informe os Numeros Novamente : ')
        n1 = int(input('Primeiro Valor : '))
        n2 = int(input('Segundo Valor : '))
        print('=-='*10)

    elif opcao == 5:
        print('Finalizando...')
        print('=-='*10)

    else :
        print('Opção Invalida, Tente Novamente')
        print('=-='*10)