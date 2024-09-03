num=[int(input('Digite um valor: ')) for numero in range(0,5)]
print('=-'*30)
print(f'Você digitou os valores {num}')
maior=menor=num[0]
for p,n in enumerate(num):
    if maior<n:
        maior=n
    if menor>n:
        menor=n
print(f'O maior valor digitado foi {maior} na posição ', end='')
for p,n in enumerate(num):
    if n==maior:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for p,n in enumerate(num):
    if n==menor:
        print(f'{p}... ', end='')