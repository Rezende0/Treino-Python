lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resp=' '
    while resp not in 'SsNn':
        resp=input('Quer continuar?[S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'A lista completa é {lista}')
par=[]
impar=[]
for p in lista:
    if p%2==0:
        par.append(p)
    else:
        impar.append(p)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')