while True:
    n=int(input('Quer a tabuada de qual número ? '))
    if n<-n:
        break
    cont=0
    print('='*30)
    while cont<=10:
        print(f'{n} x {cont} = {n*cont}')
        cont+=1
    print('='*30)
print('Fim')