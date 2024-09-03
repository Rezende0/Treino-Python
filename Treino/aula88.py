from random import randint
jogos=int(input('Quantos jogos você quer sortear? '))
print(f'SORTEANDO {jogos} JOGOS:')
sorteio=[]
for c in range(0,jogos):
    while len(sorteio)!=6:
        num=randint(1,60)
        if num not in sorteio:
            sorteio.append(num)
    print(f'Jogo {c+1}: {sorted(sorteio)}')
    sorteio.clear()