cont=soma=0
while True:
    num=int(input('Digite um número: '))
    if num==999:
        break
    soma+=num
    cont+=1
print(f'{cont} números foram escolhidos e a soma deles é igual à {soma}')