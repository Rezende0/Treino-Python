cont=soma=mais=barato=valor=0
while True:
    nome=str(input('Nome do produto: '))
    preco=float(input('Preço: R$ '))
    if preco>1000:
        mais+=1
    soma+=preco
    cont+=1
    if cont==1:
        barato=nome
        valor=preco
    else:
        if preco<valor:
            barato=nome
    final='t'
    while final not in 'SsNn':
        final=str(input('Deseja adicionar mais algum produto ?[S/N] ')).strip()[0]
    if final in 'Nn':
        break
print(f'''O gasto total de {cont} produto é de R${soma:.2f}.
{mais} produtos custam mais que R$1000,00.
O produto {barato} é o mais barato do cadastro''')