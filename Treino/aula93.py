futebol={}
temp=[]
#goltot=0
futebol['jogador']=input('Nome do jogador: ').strip().capitalize()
partidas=int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
for g in range(0,partidas):
    temp.append(int(input(f'   Quantos gols {futebol["jogador"]} fez na {g+1}° partida? ')))
futebol['gols']=temp[:]
#for c in futebol['gols']:
    #goltot+=c (função sum soma os valores numa lista)
futebol['total']=sum(temp)#goltot(substituindo goltot)
print('=-'*30)
print(futebol)
print('=-'*30)
for k,v in futebol.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {futebol["jogador"]} jogou {partidas} partidas.')
for k,v in enumerate(temp):
    print(f'   => Na {k+1}° partida, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')