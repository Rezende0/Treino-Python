tabela='Flamengo','Grêmio','Botafogo','Atlético','Palmeiras','Corinthians','Santos','Cruzeiro','Coritiba','Ponte Preta'
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os 4 últimos colocados são: {tabela[-1:-5:-1]}')
print(f'Os times em ordem alfabéticas são: {sorted(tabela)}')
print(f'O Santos está na classificação: {tabela.index('Santos')+1}ª')