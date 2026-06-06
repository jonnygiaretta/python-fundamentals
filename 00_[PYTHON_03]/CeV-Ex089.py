listage = list()
print('=-='*10)
while True : 
    name = str(input('Nome : '))
    n1 = float(input('Nota 1 : '))
    n2 = float(input('Nota 2 : '))
    media = (n1 + n2)/2
    listage.append([[name], [n1, n2], [media]])
    re = str(input('Deseja Continuar [S/N] : ')).strip().upper()[0]
    print('=-='*10)
    if 'N' in re :
        break
print(f'{"No.":<4}{"Nome":<12}{"Media":<16}')
print('=-='*10)
for a, b  in enumerate(listage) : 
    print(f'{a:<4}{b[0]:<12}{b[2]:<16.1f}')
print('=-='*10)
while True : 
    n = int(input('Deseja Mostrar as Notas de Qual Aluno (999 Interrompe): '))
    if n == 999 : 
        print('Interrompendo Programa...')
        break
    print(f'As Notas de {listage[n][0]} São Respectivamente: {listage[n][1]}')
    print('=-='*10)
print(f'{"Programa Finalizad":=^30}')