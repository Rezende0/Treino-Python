lista=[]
cadastro={}
while True:
    cadastro['nome']=input('Nome: ').strip().capitalize()
    while True:
        cadastro['sexo']=input('Sexo[M/F]: ').strip()[0]
        if cadastro["sexo"] in 'MmFf':
            break
    cadastro['idade']=int(input('Idade: '))
    lista.append(cadastro.copy())
    cadastro.clear()
    opc=' '
    while opc not in 'SsNn':
        opc=input('Quer continuuar?[S/N] ').strip()[0]
    if opc in 'Nn':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastrada.')
media=0
for c in range(0,len(lista)):
    media+=lista[c]["idade"]
print(f'B) A média de idade é de {media/len(lista):.2f}.')
print(f'C) As mulheres cadastradas foram',end='')
for k,v in enumerate(lista):
    if lista[k]["sexo"] in 'Ff':
        print(f' {lista[k]["nome"]}', end='')
print(f'\nD) Lista das pessoas que estão acima da média:')
for k,v in enumerate(lista):
    if lista[k]["idade"]>media/len(lista):
        print(f'   nome = {lista[k]["nome"]}; sexo = {lista[k]["sexo"]}; idade = {lista[k]["idade"]}')