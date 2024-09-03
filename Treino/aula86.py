list=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        list[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{list[l][c]:^10}]',end='')
    print()