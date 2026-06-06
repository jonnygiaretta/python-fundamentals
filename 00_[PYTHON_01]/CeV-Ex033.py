print('Digite um Total de 3 Valores Abaixos e Eu Irei Analiza-los Para Você')

n1 = int(input('Digite o Primeiro Valor : '))
n2 = int(input('Digite o Segundo Valor : '))
n3 = int(input('Digite o Terceiro Valor : '))

if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

print('-=-'*20)
print('Valores Analisados')
print(f'O Maior Valor Foi o de : {maior}')
print(f'O Menor Valor foi o de : {menor}')
print('-=-'*20)
