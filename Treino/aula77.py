tupla='gabriel', 'bonito', 'ama', 'laila', 'namorada'
for c in tupla:
    print(f'\nNa palavra {c} temos: ', end='')
    if c.count('a'):
        print('a', end=' ')
    if c.count('e',):
        print('e', end=' ')
    if c.count('i'):
        print('i', end=' ')
    if c.count('o'):
        print('o', end=' ')
    if c.count('u'):
        print('u', end=' ')