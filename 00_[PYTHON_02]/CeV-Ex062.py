
print('-=-'*5)

a1 = int(input('Primeiro Termo : '))
r = int(input('Razão da PA : '))
c = 1
p = 1
n = 1
cp = 0

while c <= 10 : 
    print(a1, end =' -> ')
    a1 += r
    c += 1

print('Pausa')

while n != 0 :  
    p = 1
    n = int(input('\nQuantos Termos Voce Quer Mostrar a Mais ? '))
    while p <= n :
        print(a1, end = ' -> ')
        a1 += r
        p += 1
        cp += 1
    if n != 0 :
        print('Pausa')

print(f'Progressão Finalizada com {cp+10} Termos')



