n = c = s = 0

while n != 999 : 
    n = int(input('Digite um Numero [999 para Parar]: '))
    if n != 999 : 
        s += n
        c += 1
     
print(f'Voce Digitou {c} Numeros')
print(f'A Soma Entre Eles Foi de {s}')