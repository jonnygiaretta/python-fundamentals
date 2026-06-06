
print('='*20)
print(' 10 Termos PA'.center(20))
print('='*20)

a1 = int(input('Primeiro Termo : '))
r = int(input('Razão : '))

for n in range(a1, (a1+10*r), r):
    print(n, end=' -> ')

print('Acabou')
