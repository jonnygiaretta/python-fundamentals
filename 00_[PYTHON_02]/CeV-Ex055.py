
maior = 0 
menor = 0
cma = 0
cme = 0

for c in range(1,6):
    peso = float(input(f'Peso da {c}ª Pessoa : '))
    if c == 1 : 
        maior = peso
        menor = peso
        cma = c
        cme = c
    if maior < peso : 
        maior = peso
        cma = c
    if menor > peso : 
        menor = peso
        cme = c

print(f'O Maior Peso Registrado Foi da {cma}ª Pessoa, Pesando : {maior:.1f}Kg')
print(f'O Menor Peso Registrado Foi da {cme}ª Pessoa, Pesando : {menor:.1f}Kg')