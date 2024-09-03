from time import sleep
def lin():
    print('=-'*30)
def contagem(i,f,t):
    lin()
    if t<0:
        print(f'Contagem de {i} até {f} de {t*-1} em {t*-1}:')
    else:
        print(f'Contagem de {i} até {f} de {t} em {t}:')
    if f>=0:
        f+=1
    else:
        f-=1
    #sleep(2)
    for c in range(i,f,t):
        print(f'{c} ',end='',flush=True)
        #sleep(0.4)
    print('Fim!',end='')
    print()
contagem(1,10,1)
contagem(10,0,-2)
lin()
print('Agora é sua vez de personalizar a contagem!')
contagem(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))