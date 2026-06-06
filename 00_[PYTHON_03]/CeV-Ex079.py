list = []

print('=-='*10)

while True :
    
    n = int(input('Digite Um Valor : '))
    
    if n not in list:
        list.append(n)
    else : 
        print('Valor Duplicado! Não Será Adicionado a Listagem.')
    re = str(input('Deseja Continuar [S/N] : '))
    re = re.strip().upper()[0]
    if re == 'N' :
        break
    
print('=-='*20)
for i, v in enumerate(list) : 
    print(f'Voce Digitou o Valor : [{v}] // Na Posição : [{i+1}]')
    
print('=-='*20)