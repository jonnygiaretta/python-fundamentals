n = 0
num = [[], []]
print('=-='*10)
for c in range(1,8) : 
    n = int(input(f'Digite o {c}o. Valor : '))
    if n % 2 == 0 : 
        num[0].append(n)
    else : 
        num[1].append(n)
print('=-='*20)
num[0].sort()
num[1].sort()
print(f'Os Valores Pares Digitados Foram : {num[0]}')
print(f'Os Valores Impares Digitados Foram : {num[1]}')
print('=-='*20)