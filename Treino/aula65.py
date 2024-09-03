sair='S'
cont=soma=0
while sair not in 'Nn':
    num=int(input('Digite um número: '))
    cont+=1
    soma+=num
    if cont==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    sair=str(input('Quer continuar ? [S/N] ')).strip()[0]
    while sair not in 'SsNn':
        print('Digite um valor válido!')
        sair=str(input('Quer continuar ? [S/N] ')).strip()[0]
print(f'Você digitou {cont} números e a média foi {soma/cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')