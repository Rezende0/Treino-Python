listum=[]
par=[]
impar=[]
for c in range(1,8):
    n=int(input(f'Digite o {c}° valor: '))
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
listum.append(par)
listum.append(impar)
print('=-'*30)
print(f'Os valores pares digitador foram: {sorted(listum[0])}')
print(f'Os valores ímpar digitador foram: {sorted(listum[1])}')