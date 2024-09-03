from datetime import date
atual=date.today().year
contratraçao={}
while True:
    contratraçao['nome']=input('Nome: ').strip().capitalize()
    contratraçao['idade']=atual-int(input('Ano de Nascimento: '))
    contratraçao['ctps']=int(input('Carteira de Trabalho (0 = não tem): '))
    if contratraçao["ctps"]==0:
        break
    contratraçao['contratação']=int(input('Ano de Contratação: '))
    contratraçao['salario']=float(input('Salário: '))
    temptrabalhado=atual-contratraçao['contratação']
    contratraçao['aposentadoria']=40-temptrabalhado
    break
print('=-'*30)
for k,v in contratraçao.items():
    print(f'- {k} tem o valor {v}.')