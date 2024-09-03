aluno=[]
temp=[]
while True:
    temp.append(input('Nome: ').strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1]+temp[2])/2)
    aluno.append(temp[:])
    temp.clear()
    resp=' '
    while resp not in 'SsNn':
        resp=input('Deseja continuar?[S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{'No.':<4}{'NOME':<10}{'MÉdia':>8}')
print('-'*26)
for n,v in enumerate(aluno):
    print(f'{n:<4}{v[0]:<10}{v[3]:>8.1f}')
num=' '
while num!=999:
    print('=-'*30)
    num=int(input('Mostrar nota de qual aluno (999 interrompe)? '))
    for n,v in enumerate(aluno):
        if num==n:
            print(f'As notas de {v[0]} são {v[1],v[2]}.')