jogador={}
futebol=[]
while True:
    jogador['nome']=input('Nome do Jogador: ').strip().upper()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    temp=[]
    for g in range(0,partidas):
        temp.append(int(input(f'Quantos gols na {g+1}° partida? ')))
    jogador['gols']=temp[:]
    jogador['total']=sum(temp)
    futebol.append(jogador.copy())
    while True:
        opc=input('Quer continuar?[S/N] ').strip()[0]
        if opc in 'SsNn':
            break
    if opc in 'Nn':
        break
print('=-'*30)
#print('cod nome        gols          total')fiz assim
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(futebol):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    valor=int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if valor==999:
        break
    if valor>=len(futebol):
        print(f'ERRO! Não existe jogador com tal código.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {futebol[valor]["nome"]}:')
        for i,g in enumerate(futebol[valor]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)