from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento : '))
idade = (atual - nascimento)

print(f'O Atleta Tem {idade} Anos.')

if idade > 25 : 
    print('Classificação : Master ')

elif idade <= 25 and idade > 19 :
    print('Classificação : Sênior ')
    
elif idade <= 19 and idade > 14 :
    print('Classificação : Júnior ')
    
elif idade <= 14 and idade >= 9 :
    print('Classificação : Infantil ')
    
elif idade < 9 : 
    print('Classificação : Mirim ')