def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param n: uma ou mais notas do aluno (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação do aluno.
    """
    pontos={}
    pontos['Total']=len(n)
    pontos['Maior']=max(n)
    pontos['Menor']=min(n)
    #for v,c in enumerate(n):
        #if v==0 or c>maior:
            #maior=c
        #if v==0 or c<menor:
            #menor=c
    #pontos['Maior']=maior
    #pontos['Menor']=menor
    pontos['Média']=sum(n)/len(n)
    if sit==True:
        if pontos["Média"]>=7:
            pontos['Situação']='Boa'
        else:
            pontos['Situação']='Ruim'
    return pontos
#Programa Principal
resp=notas(5,7,10,7,sit=True)
print(resp)
print()
help(notas)