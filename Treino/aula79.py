lista=[]
while True:
    n=int(input('Digite um Valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor dupliucado! Não vou adicionar...')
    resposta=' '
    while resposta not in 'SsNn':
        resposta=str(input('Quer continuar? ')).strip()[0]
    if resposta in 'Nn':
        break
lista.sort()
print(f'Você Digitou os valores {lista}')