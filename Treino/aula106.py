c=('\33[m',           #0-Sem cor
   '\33[0;34m',       #1 -azul 
   '\33[0;37m',       #2 - branco
   '\33[0;32m',       #3 - verde
   '\33[0;31m',       #4 - vermelho
   '\33[0;33m'        #5 - amarelo
   )


def estilo(r,cor=0):
    print(c[cor], end='')
    print('~'*(len(r)+4))
    print(f'  {r}')
    print('~'*(len(r)+4))
    print(c[0], end='')


def pyhelp(msg):
    while True:
        estilo('SISTEMA DE AJUDA PyHELP',3)
        f=input(msg).strip()
        if f.lower()=='fim':
            print(c[4])
            print('Programa encerrado!')
            break
        estilo(f"Acessando o manual do comando '{f}'",1)
        print(c[5])
        help(f)


#Programa Principal  
pyhelp('função ou biblioteca (digite fim para encerrar) > ')