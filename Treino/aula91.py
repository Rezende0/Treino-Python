from random import randint
jogo={'Jogador 1' : randint(1,6),
'Jogador 2' : randint(1,6),
'Jogador 3' : randint(1,6),
'Jogador 4' : randint(1,6)}
rank=[]
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
rank=sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('\n== RANKING DOS JOGADORES ==\n')
for i,c in enumerate(rank):
    print(f'{i+1}° lugar: {c[0]} com {c[1]}')