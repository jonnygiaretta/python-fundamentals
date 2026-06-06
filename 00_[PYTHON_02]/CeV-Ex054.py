
from datetime import date

atual = date.today().year
maior = 0

for c in range(1,8):
    data = int(input(f'Em Que Ano a {c}ª Pessoa Nasceu : '))
    if (atual - data) >= 18 :
        maior = maior + 1
    
print(f'Ao Todo Tivemos {maior} Pessoas Maiores de Idade')
print(f'Ao Todo Tivemos {7 - maior} Menores de Idade')
        
