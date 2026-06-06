
times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR',
         'Flamengo', 'Coritiba', 'Atlético-MG', 'Botafogo', 'Vasco', 
         'Grêmio', 'Bragantino', 'Vitória', 'Santos', 'Corinthians', 
         'Internacional', 'Chapecoense', 'Cruzeiro', 'Mirassol', 'Remo')


print('=-='*25)
print(f'Lista dos Times do Brasileirão Serie A {times}')
print('=-='*25)
print(f'Os Cinco Primeiros Times São : {times[:5]}')
print('=-='*25)
print(f'Os Quatro Ultimos Times São : {times[-4:]}')
print('=-='*25)
print(f'Os Times em Ordem Alfabetica São : {sorted(times)}')
print('=-='*25)
print(f'A Chapecoense Está na {times.index('Chapecoense') + 1}ª')
print('=-='*25)