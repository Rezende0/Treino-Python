num=[]
while True:
    num.append(int(input('Digite um valor: ')))
    resp=' '
    while resp not in 'SsNn':
        resp=input('Quer continuar?[S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}.')
if num.count(5)>=1:
    print('O valor 5 foi encontrado na lista')
else:
    print(f'O valor 5 não foi encontrado na lista')