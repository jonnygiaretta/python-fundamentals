s = 0
cg = 0
cp = 0

for c in range(1,7):
    cg = cg + 1
    n = int(input(f'Digite {c}o Valor : '))
    if n % 2 == 0 : 
        s = s + n
        cp = cp + 1

print(f'De {cg} Valores Digitados, Existiam {cp} Valores Pares \nA Soma Deles Foi De : {s}')