aluno=dict()
lista=list()
while True:
    aluno['nome']=input('Nome: ').strip().capitalize()
    aluno['média']=float(input('Média: '))
    if aluno['média']<=10 and aluno['média']>=0:
        if aluno["média"]<7 and aluno["média"]>=0:
            aluno['situação']='REPROVADO'
        elif aluno["média"]>=7 and aluno["média"]<=10:
            aluno['situação']='APROVADO'
    lista.append(aluno.copy())
    opc=' '
    while opc not in 'SsNn':
        opc=input('Deseja consultar mais algum aluno?[S/N] ').strip()[0]
    if opc in 'Nn':
        break
print('=-'*30)
for c in range(0,len(lista)):
        print(f'{lista[c]["nome"]} teve média de {lista[c]["média"]}, portanto, está {lista[c]["situação"]}.')