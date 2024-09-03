n=int(input('Digite quantos termos voce quer mostrar: '))
cont=0
t1=0
t2=1
if n==1:
    print(f'{t1}')
elif n==2:
    print(f'{t1} → {t2}')
else:
    print(f'{t1} → {t2} →', end=' ')
    cont=3
    while cont<=n:
        t3=t2+t1
        print(t3,'→ ' if cont<n else '', end='')
        t1=t2
        t2=t3
        cont+=1
print('Fim')