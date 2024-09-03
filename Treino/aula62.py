aum=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=1
mais=10
total=0
while mais!=0:
    total+=mais
    while not cont>total:
        print(aum,' → ' if cont<total else '' ,end='')
        aum+=razao
        cont+=1
    mais= int(input('Deseja mais quantos termos ? '))