c = pares = 0

valores = ( int(input('Digite um Valor : ')),
        int(input('Digite um Valor : ')), 
        int(input('Digite um Valor : ')), 
        int(input('Digite um Valor : ')) )
        
while c > 5 : 
    if valores % 2 == 0 : 
        pares += 1
    c += 1
        
print('=-='*10)
print('Valores Digitados : ')
print('=-='*10)
print(valores)
print('=-='*10)
print(f'o Valor Nove Apareceu {valores.count(9)} Vezes')
print('=-='*10)
if 3 in valores : 
    print(f'o Valor Tres Apareceu na {valores.index(3)+1}ª Posição ')
else : 
    print('O Valor 3 Não Foi Digitado em Nenhuma Posição')
print('=-='*10)
print(f'Ao Todo Foram Digitados {pares} Valores Pares. ')
print('=-='*10)