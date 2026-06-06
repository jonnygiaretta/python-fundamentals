info = dict()
print('=-='*10)
info['Nome'] = str(input('Nome : '))
info['Media'] = int(input(f'Media de {info["Nome"]}: '))
print('=-='*10)
if info["Media"] >= 7 : 
    info['Situacao'] = str('Aprovado')
else : 
    info['Situacao'] = str('Reprovado')
for k, v in info.items():
    print(f'- {k} é Igual a {v}')
print('=-='*10)