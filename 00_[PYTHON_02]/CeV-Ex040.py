n1 = float(input('Primeira Nota : '))
n2 = float(input('Segunda Nota : '))
m = (n1+n2)/2

if m >= 7:
    print(f'Tirando {n1:.1f} & {n2:.1f}, Sua Media é : {m:.1f}')
    print('O Aluno Está Aprovado')

elif m >= 5 and m <= 6.9:
    print(f'Tirando {n1:.1f} & {n2:.1f}, Sua Media é : {m:.1f}')
    print('O Aluno Está em Recuperação')
    
elif m < 5:
    print(f'Tirando {n1:.1f} & {n2:.1f}, Sua Media é : {m:.1f}')
    print('O Aluno Está Reprovado')