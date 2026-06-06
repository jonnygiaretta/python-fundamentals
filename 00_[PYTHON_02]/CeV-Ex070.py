
soma = c1000 = menor =  0

print('-'*30)
print('Super Loja Baratão'.center(30))
print('-'*30)

while True : 

    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    if soma == 0 :
        menor = preco
        nomemenor = nome
    soma += preco

    if preco > 1000 : 
        c1000 += 1
    if preco < menor : 
        menor = preco   
        nomemenor = nome


    opcao = ' '

    print('-'*30)
    while opcao not in 'SN' :
        opcao = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    print('-'*30)
    
    if opcao in 'N' : 
        break

print('{:-^30}'.format('Fim das Compras'))
print('-'*30)

print(f'O Total das Suas Compras Foi de R${soma:.2f}')
print(f'Temos {c1000} Custando Mais de R$1000.00')
print(f'O Produto Mais Barato Foi {nomemenor}, Custando {menor:.2f}')
print('-'*30)



