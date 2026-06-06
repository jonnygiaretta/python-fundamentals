
s = c = 0

while True : 
    n = int(input('Digite um Valor (999 Para Parar) : '))
    if n == 999 : 
        break
    s += n
    c += 1

print(f'A Soma Dos {c} Valores Foi de {s}')