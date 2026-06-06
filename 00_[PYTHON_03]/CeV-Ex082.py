catalog = []
catalogods = []
catalogeven = []

print('=-='*15)
while True : 
    n = int(input('Digite um Valor : '))
    catalog.append(n)
    
    re = str(input('Deseja Continuar [S/N] : '))
    re = re.strip().upper()[0]
    print('=-='*15)

    if re == 'N' :
        break
    if re != 'S' :
        while True : 
            print('=-='*15)
            print('Comando de Continuidade Incorreto! Digite Novamente.')
            re = str(input('Deseja Continuar [S/N] : '))
            print('=-='*15)
            re = re.strip().upper()[0]
            if re == 'S' or re == 'N' : 
                break

for i, n in enumerate(catalog) : 
    if n % 2 == 0 : 
        catalogods.append(n)
    else : 
        catalogeven.append(n)

print(f'Voce Digitou os Seguintes Valores na Sua Lista Geral : ')
print('=-='*15)
for i, n in enumerate(catalog) : 
    print(f'O Valor [{n}] <//> [{i+1}]ª Posição')
print('=-='*15)
print(f'Os Valores Pares da Sua Lista Geral São : ')
print('=-='*15)
for i, n in enumerate(catalogods) : 
    print(f'O Valor [{n}] <//> [{i+1}]ª Posição')
print('=-='*15)
print(f'Os Valores Impares da Sua Lista Geral São : ')
print('=-='*15)
for i, n in enumerate(catalogeven) : 
    print(f'O Valor [{n}] <//> [{i+1}]ª Posição')
print('=-='*15)