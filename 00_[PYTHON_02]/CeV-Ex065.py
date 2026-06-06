
opcao = 'S'
soma = cont = 0

while opcao in 'Ss' : 
    n = int(input('Digite um Numero : '))
    opcao = str(input('Quer Continuar ? [S/N] '))
    soma += n  
    cont += 1

    if cont == 1 : 
        maior = menor = n
    if n < menor : 
        menor = n
    if n > maior : 
        maior = n
    
print(f'Voce Digitou {cont} Numeros & a Media Entre Eles Foi : {(soma/cont):.3f}')
print(f'O Maior Valor Entre Eles Foi {maior} & O Menor Valor Foi {menor}')
