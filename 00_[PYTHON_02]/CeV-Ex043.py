
peso = float(input('Digite Seu Peso (Kg) : '))
altura = float(input('Digite Sua Altura (m) : '))
imc = (peso) / (altura ** 2)


print(f'O IMC Destá Pessoa é de {imc:.2f}')

if imc > 40 : 
    print('Categorizado Como : Obesidade Morbida')

elif imc <= 40 and imc >= 30 : 
    print('Categorizado Como : Obesidade')

elif imc <= 30 and imc >= 25 : 
    print('Categorizado Como : Sobrepeso')

elif imc <= 25 and imc >= 18.5 : 
    print('Categorizado Como : Peso Ideal')

if imc < 18.5 : 
    print('Categorizado Como : Abaixo do Peso')
