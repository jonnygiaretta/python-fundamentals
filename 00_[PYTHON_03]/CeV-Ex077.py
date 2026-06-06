
palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

print('=-='*20)
for p in palavras : 
    print(f'\n Na Palavra {p.strip().upper()}, Temos as Seguintes Vogais Ordenadas : ', end = '')

    for letra in p : 
        if letra.lower() in 'aeiou' : 
            print(letra, end = ' ') 
print('\n', '=-='*20)
