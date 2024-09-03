tupla='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
contagem=30
while not 0<=contagem<=20:
    contagem=int(input('Digite um número entre 0 a 20: '))
num=tupla[contagem]
print(f'Você digitou o número {num}')