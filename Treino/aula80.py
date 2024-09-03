valores=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n>valores[-1]:
        valores.append(n)
        print(f'O valor {n} foi adicionado na posição final')
    else:
        pos=0
        while pos<len(valores):
            if n<=valores[pos]:
                valores.insert(pos,n)
                print(f'O número {n} foi adicionado na posição {pos}')
                break
            pos+=1
print('=-'*30)
print(f'Você digitou os número {valores}')