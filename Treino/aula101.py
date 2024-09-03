def voto(nasc):
    from datetime import date
    idade=date.today().year-nasc
    if idade<16:
        return f'Com {idade} anos: NÃO PODE VOTAR!'
    elif idade<18 or idade>=75:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
print(voto(int(input('Ano de Nascimento: '))))