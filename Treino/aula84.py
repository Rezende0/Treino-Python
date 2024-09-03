listum=[]
listdois=[]
while True:
    listdois.append(input('Nome: '))
    listdois.append(float(input('Peso: ')))
    listum.append(listdois[:])
    listdois.clear()
    cad=' '
    while cad not in 'SsNn':
        cad=input('Deseja cadastrar mais alguem?[S/N] ').strip()[0]
    if cad in 'Nn':
        break
maior=menor=listum[0][1]
for c in listum:
    if c[1]>maior:
        maior=c[1]
    if c[1]<menor:
        menor=c[1]     
print('=-'*30)
print(f'Foram cadastradas {len(listum)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in listum:
    if p[1]==maior:
        print(f'[{p[0]}]',end=' ')
print(f'\nO menor peso foi de {menor}. Peso de ', end='')
for m in listum:
    if m[1]==menor:
        print(f'[{m[0]}]',end=' ')