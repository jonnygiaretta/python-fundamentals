
print('-=-'*5)

a1 = int(input('Primeiro Termo : '))
r = int(input('Razão da PA : '))
n = a1
c = 1

while c <= 10 : 
    print(n, end = ' -> ')
    n += r
    c += 1

print('Acabou')