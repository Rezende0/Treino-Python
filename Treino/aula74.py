from random import randint
maior=menor=' '
cont=0
a=randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20)
print('Os valores sorteados foram: ', end=' ')
for b in a:
    print(b, end=' ')
    cont+=1
    if cont==1 or b>maior:
        maior=b
    if cont==1 or b<menor:
        menor=b
print(f'\nO maior número é {maior}')
print(f'O menor numero é {menor}')