
frase = str(input('Digite Uma Frase : '))

frasemod = frase.replace(' ', '')
frasemod = frasemod.upper()
frasemod = frasemod[::-1]

frase = frase.upper()
frase = frase.replace(' ', '')

print(f'O Inverso de {frase} é {frasemod}')
if frase == frasemod :
    print('Temos Um Palindromo')
else : 
    print('A Frase Digitada Não é Um Palindromo')

