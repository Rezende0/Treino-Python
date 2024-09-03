from random import randint


def sorte(r):
    print(f'Sorteando 5 valores da lista: ',end='')
    for n in r:
        print(f'{n} ',end='')
    print('PRONTO!') 


def par(p):
    soma=0
    for n in p:
        if n%2==0:
            soma+=n
    print(f'Somando os valores pares de {p}, temos {soma}')


lista=[randint(1,10) for a in range(0,5)]
sorte(lista)
par(lista)