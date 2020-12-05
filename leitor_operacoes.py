#leitor lista operacoes

import os


def ler_arquivo(endereco, arquivo):

    if os.getcwd() != os.path.join(endereco):
        os.chdir(os.path.join(endereco))

    linhasarq = open(arquivo)

    linhas = linhasarq.readlines()

    return linhas

def ler_tabelas(linhas):

    #procs[1]

    blocos = int(linhas[0])

    segmentos = int(linhas[1])

    tabela=[]

    for lin in linhas[2:(segmentos+2)]:
        dados={}
        coluna=lin.split(', ')
        dados['arq']=coluna[0]
        dados['bl_inicio']=int(coluna[1])
        dados['bl_tam']=int(coluna[2])
        tabela=tabela+[dados]

    return tabela

def ler_tabs(linhas):

    tab = []

    segmentos = int(linhas[1])

    for lin in linhas[(segmentos+2):]:
        dados = {}
        coluna = lin.split(', ')
        dados['proc'] = coluna[0]
        dados['oper'] = coluna[1]
        dados['arq'] = coluna[2]
        if int(dados['oper']) == 0:
            dados['blocos']=coluna[3]
        tab=tab+[dados]
    return tab

def main(endereco, arquivo):
    linhas = ler_arquivo(endereco, arquivo)
    tabela = ler_tabelas(linhas)
    tab = ler_tabs(linhas)

    print(tabela)
    print(tab)