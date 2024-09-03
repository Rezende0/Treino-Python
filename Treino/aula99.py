from time import sleep
def val(*n):
    print('=-'*30)
    print('Analisando os valores passados...')
    sleep(1.5)
    maior=0#caso nao tenha casas fazias, pode tirar
    for p,c in enumerate(n):
        if p==0 or c>maior:
            maior=c
        print(f'{c} ',end='')
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
        
val(2,9,4,5,7,1)
val(4,7,0)
val(1,2)
val(6)
val()