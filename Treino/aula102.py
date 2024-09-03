def fatorial(fat,show=False):
    """
    -> Calcula o fatorial de um número.
    :param fat: número a ser fatorado.
    :param show: False para não mostrar o processo de fatoração e True para mostrar.
    :return: O número fatorado com ou sem o processo de cálculo.
    """
    f=1
    print('-'*30)
    for c in range(fat,0,-1):
        f*=c
        if show==True:
            print(f'{c} x ' if c!=1 else f'{c} = ',end='')
    return f'{f}'
print(fatorial(5,True))