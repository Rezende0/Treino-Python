expr=input('Digite sua expressão: ')
lista=[]
for verif in expr:
    if verif in '()':
        lista.append(verif)
if lista.count('(')==lista.count(')'):
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')