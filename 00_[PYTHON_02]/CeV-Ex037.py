n = int(input('Digite um Numero Inteiro : '))

print('Escolha a Base Para Conversão : ')
print('[1] : Converter Para BINÁRIO')
print('[2] : Converter Para OCTAL')
print('[3] : Converter Para HEXADECIMAL')

opcao = int(input('Sua Opção : '))

if opcao == 1:
    print(f'({n})10 Convertido para Binario Equivale :({bin(n)[2:]})2 ')
elif opcao == 2:
    print(f'({n})10 Convertido para Binario Equivale :({oct(n)[2:]})8 ')
elif opcao == 3:
    print(f'({n})10 Convertido para Binario Equivale :({hex(n)[2:]})16 ')
else:
    print('Opção Invalida, Tente Novamente')
