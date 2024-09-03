def area(l,c):
    print(f'A área de um terreno com dimensão {l:.1f}m x {c:.1f}m é de {l*c:.1f}m².')
print()
print(' Controle de Terrenos')
print('-'*21)
area(float(input('Largura (m): ')),float(input('Comprimento (m): ')))