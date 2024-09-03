def ficha(nome,gols):
    if nome=='':
        nome='<Desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
print('-'*30)
ficha(input('Nome do Jogador: ').strip().capitalize(),(input('Número de Gols: ')))