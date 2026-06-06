f = input('Digite Seu Nome Completo ')
f = f.strip()
d = f.split()
h = (len(f) - f.count(' '))

print(f'Seu Nome Com Todas as Letras Maisculas :  {f.upper()}')
print(f'Seu Nome Com Todas as Letras Minusculas :  {f.lower()}')
print(f'Seu Nome Sem Espaços Tem : {h} Caracteres')
print(f'Seu Primeiro Nome Tem {len(d[0])} Caracteres')
