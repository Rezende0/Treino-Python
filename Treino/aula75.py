tupla=(int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')))
if tupla.count(9):
    print(f'O número 9 apareceu {tupla.count(9)}')
if tupla.count(3):
    print(f'O número 3 aparece na posição {tupla.index(3)+1}')
print('Os valores pares digitados foram:',end=' ')
for n in tupla:
    if n%2==0:
        print(n,end=' ')