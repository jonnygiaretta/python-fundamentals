
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
              'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
                'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito','Dezenove',
                  'Vinte')

re = 'S'

while 'S' in re : 

    n = int(input('Digite um Numero Entre 0 a 20 : '))

    if n >= 0 and n <= 20 : 
        print(f'Voce Digitou o Numero {numeros[n]}')
    else : 
        print('Entrada Incorreta, Tente Novamente')
    
    re = str(input('Voce Deseja Continuar [S/N]: ')).strip().upper()[0]

print('Programa Finalizado Com Sucesso.')