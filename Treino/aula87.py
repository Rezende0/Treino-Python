matriz=[[],[],[]]
soma=coluna=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
        if matriz[l][c]%2==0:
            soma+=matriz[l][c]
        if c==2:
            coluna+=matriz[l][2]
        if l==1:
            if c==0 or matriz[l][c]>maior:
                maior=matriz[l][c]
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]',end='')
    print()
print()
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores na terceira coluna é {coluna}.')
print(f'O maior valor da segunda linha é {maior}.')