maior=homem=mulher=0
while True:
    idade=int(input('Idade: '))
    if idade>18:
        maior+=1
    sexo='h'
    while sexo not in 'MmFf':
        sexo=str(input('Sexo[M/F]: ')).strip()[0]
    cad='f'
    while cad not in 'SsNn':
        cad=str(input('Deseja cadastrar mais alguem ?[S/N] ')).strip()[0]
    if sexo in 'Mm':
        homem+=1
    if idade<20 and sexo in 'Ff':
        mulher+=1
    if cad in 'Nn':
        break
print(f'''{maior} pessoas tem mais de 18 anos.
{homem} homens foram cadastrados.
{mulher} mulheres tem menos de 20 anos.''')