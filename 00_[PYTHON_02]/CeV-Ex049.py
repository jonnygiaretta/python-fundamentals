
n = int(input('Digite um Numero Para Ver Sua Tabuada : '))

print('-=-'*5)
print(f' TABUADA DO {n} ')
print('-=-'*5)
for c in range (1,11):
    print(f'{n} x {c} = {n*c}')
print('-=-'*5)