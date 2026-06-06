num = []
print('=-='*20)
for c in range(0,5) : 
    num.append(int(input(f'Digite um Valor para a Posição [{c+1}ª] : ')))
print('=-='*20)

maior = max(num)
menor = min(num)

print('Voce Digitou os Seguintes Valores : ')
print('=-='*20)
for c in range(0,5) : 
    print(f'Voce Digitou o Valor [{num[c]}] na [{c+1}ª] Posição')

print('=-='*20)
print(f'O Maior Valor Digitado Foi : [{maior}], Nas Posições : ', end = '')
for a, b in enumerate(num) : 
    if b == maior :
        print(f'[{a+1}]ª', end = ' ')
print(f'\nO Menor Valor Digitado Foi : [{menor}], Nas Posições : ', end = '')
for a, b in enumerate(num) : 
    if b == menor:
        print(f'[{a+1}]ª', end = ' ')
print()
print('=-='*20)