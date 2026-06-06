geral = list()
info = dict()
womans = list()
re = 'S'
s = 0
print('=-='*15)
while True : 
    while re not in 'SN':  
        print('-> Comando de Continuidade Digitado Incorretamente')
        re = str(input('-> Deseja Continuar [S/N] : ')).strip().upper()[0]
        if re in 'SN':  
            break
    if re == 'N':
        break
    name = str(input('-> Digite Seu Nome : '))
    info['Nome'] = name
    info['Sexo'] = str(input('-> Sexo [M/F] : ')).strip().upper()[0]
    info['Idade'] = int(input('-> Idade : '))
    re = str(input('-> Deseja Continuar [S/N] : ')).strip().upper()[0]
    geral.append(info.copy())
    info.clear()
    print('=-='*15)
for p in geral : 
    s += p['Idade']
m = s/len(geral)
for w in geral : 
    if w['Sexo'] == 'F':
        womans.append(w['Nome'])
print(f'-> O Grupo Tem Um Total de [{len(geral)}] Pessoas')
print(f'-> A Media de Idade do Grupo é de [{m:.2f}] Anos de Idade')
print(f'-> As Mulheres Cadastrada do Grupo Foram : ', end ='')
for w in womans:
    print(f'[{w}]', end = ' ')
print()
print('=-='*15)
print('  << Lista de Pessoas Que Estão Acima da Media >>')
print('=-='*15)
for p in geral : 
    print('=-='*15)
    if p['Idade'] >= m:
        for a, b in p.items() : 
            print(f'-> {a} = {b}')
print('=-='*15)
