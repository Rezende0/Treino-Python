num=soma=cont=0
num=int(input('Digite um número[999 para parar]: '))
while not num==999:
    soma+=num
    cont+=1
    num=int(input('Digite um número[999 para parar]: '))
print(f'Você digitou {cont} número e a soma de todos eles é {soma}')