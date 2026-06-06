s = 0 
c = 0

for n in range(3, 500, 3):
    if n % 2 != 0 : 
        s = s + n
        c = c + 1

print(f'A Soma de Todos os {c} Valores Solicitados Vale : {s}')