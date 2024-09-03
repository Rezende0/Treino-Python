tabela=('Alho','20,00/Kg',
'Banana',5,
'Café',5,
'Macarrão',3)
for n in range(0, len(tabela)):
    if n%2==0:
        print(f'{tabela[n]:.<30}', end='')
    else:
        print(f'R${tabela[n]:>10}')