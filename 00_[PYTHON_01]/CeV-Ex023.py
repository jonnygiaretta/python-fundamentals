n = int(input('Informe um Numero : '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Analise do Numero : {n}')
print(f'Unidade : {u:.0f}')
print(f'Dezena : {d:.0f}')
print(f'Centena : {c:.0f}')
print(f'Milhar : {m:.0f}')