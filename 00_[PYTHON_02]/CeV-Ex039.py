from datetime import date

atual = date.today().year
nascimento = int(input('Digite o Seu Ano de Nascimento : '))
idade = (atual - nascimento)
dif = abs(18 - idade)

if idade < 18:
    print(f'Quem Nasceu em {nascimento} tem {idade} Anos em {atual}')
    print(f'Ainda Faltam {dif} Anos Para o Seu Alistamento')
    print(f'Seu Alistamento Será em {(atual + dif)}')
elif idade > 18:
    print(f'Quem Nasceu em {nascimento} tem {idade} Anos em {atual}')
    print(f'Voce Ja Deveria Ter Realizado o Seu Alistamento a {dif} Anos ')
    print(f'Seu Alistamento Foi em {(atual - dif)}')
elif idade == 18:
    print(f'Quem Nasceu em {nascimento} tem {idade} Anos em {atual}')
    print(f'Voce Deve Comparecer a Uma Junta Militar e Se Alistar Imediatamente ')
