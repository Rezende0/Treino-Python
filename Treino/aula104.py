def leiaInt(msg):
    while True:
        n=str(input(msg)).strip()
        if n.isnumeric():
            valor=int(n)
            return valor
        else:
            print('\033[0;31mErro! Valor inválidado\033[m')
n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')