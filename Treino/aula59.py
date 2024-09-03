from math import factorial
primeiro=int(input('\33[36mDigite um número para calcular seu fatorial: \33[m'))
fac=factorial(primeiro)
segundo=0
print(fac)
opcao=0
while not opcao==3:
    print('''\33[36m[ 1 ] calcular fatorial
[ 2 ] novos número
[ 3 ] Sair do progrma\33[m''')
    opcao=int(input('\33[33mQual opção deseja ? \33[m'))
    if opcao==1:
        print(f'\33[35mO valor {primeiro} + {segundo} é igual a {primeiro+segundo}.\33[m')
    elif opcao==2:
        print(f'\33[35mO valor {primeiro} x {segundo} é igual a {primeiro*segundo}.\33[m')
    else:
        print('\33[31mOpção inválida.\33[m')
    print('=-='*20)
print('Programa encerrado!')