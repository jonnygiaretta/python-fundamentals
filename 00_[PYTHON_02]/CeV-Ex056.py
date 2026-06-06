
si = 0
imm = 0
mm20 = 0

for c in range(1, 5):
    print(f'----{c}ª Pessoa----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))

    si = si + idade
    if sexo == 'M' :
        if idade > imm : 
            imm = idade
            immn = nome
    if sexo == 'F' :
        if idade < 20 : 
            mm20 = mm20 + 1

print(f'A Media de Idade do Grupo : {(si/c):.2f} ')
print(f'O {immn} é o Homem Mais Velho, Tendo {imm} Anos ')
print(f'Ao Todo Neste Grupo Tem {mm20} Mulheres Com Menos de 20 Anos')


