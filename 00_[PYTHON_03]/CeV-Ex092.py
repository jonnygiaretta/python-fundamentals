from datetime import date
person = list()
info = dict()
print('=-='*15)
info['Nome'] = (str(input('- Nome : ')))
info['Nascimento'] = (int(input('- Ano de Nascimento : ')))
info['CTPS'] = (int(input('- Carteira de Trabalho [Digite 0 <//> Não Tem] : ')))
if info['CTPS'] == 0 : 
    print('=-='*15)
    print('  == Dados Digitados ==')
    print('=-='*15)
    person.append(info.copy())
    for a, b in info.items() : 
        print(f'- {a} Tem o Valor {b}')
else : 
    info['Contratacao'] = (int(input('- Ano de Contratação : ')))
    info['Salario'] = (int(input('- Salario  : R$ ')))
    anoatual = date.today().year
    info['Idade'] = int(anoatual - info['Nascimento'])
    info['Aposentadoria'] = int(35 + (info['Contratacao'] - info['Nascimento']))
    person.append(info.copy())
    print('=-='*15)
    print('   == Dados Digitados ==')
    print('=-='*15)
    for a, b in info.items() : 
        print(f'- {a} Tem o Valor {b}')
    print('=-='*15)
    