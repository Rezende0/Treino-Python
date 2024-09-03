from random import randint
v=0
print('Vamos jogar par ou ímpar')
while True:
    computador=randint(0,10)
    jogador=int(input('Digite um valor: '))
    total= jogador + computador
    tipo=' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Ímpar ? [P/I] ')).strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total é {total}')
    print('Deu PAR' if total%2==0 else 'Deu ÍMPAR')
    if tipo in 'Pp':
        if total%2==0:
            print('Você VENCEU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    elif tipo in 'Ii':
        if total%2==1:
            print('Você VENCEU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')