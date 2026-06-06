
n = int(input('Digite Um Numero, Para Saber Seu Fatorial : '))
fact = 1
print(f'O Fatorial de {n} : ', end ='' )
print(f'{n}! = ', end = '')

while n !=0 : 
    if n > 1 : 
        print(n, end = ' x ')
    else : print(n, end = '')
    fact = n * fact
    n  = n - 1 

print(f' = {fact}')