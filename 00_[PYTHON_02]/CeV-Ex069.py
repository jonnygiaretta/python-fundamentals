chomem = cmaior18 = cmulher20 = idade = 0
sexo = opcao = ' '

while True : 
    
    print('-'*30)
    print('Cadastre Uma Pessoa'.center(30))
    print('-'*30)

    idade = int(input('Idade: '))
    while sexo not in 'MF' :
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if sexo in 'M':
        chomem += 1
    elif idade < 20:
        cmulher20 += 1
    if idade > 18:
        cmaior18 += 1
    
    print('-'*30)
    while opcao not in 'SN' :
        opcao = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
    print('-'*30)
    
    if opcao in 'N':
        break

print(f'Total de Pessoas +18 Cadastradas : {cmaior18}')
print(f'Total de Homens Cadastrados : {chomem}')
print(f'Total de Mulheres -20 Cadastradas : {cmulher20}')
print('-'*30)

    