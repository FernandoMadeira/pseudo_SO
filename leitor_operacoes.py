#leitor lista operacoes

import os
import gerenciador_memoria


def ler_arquivo(endereco, arquivo):

    if os.getcwd() != os.path.join(endereco):
        os.chdir(os.path.join(endereco))

    linhasarq = open(arquivo)

    linhas = linhasarq.readlines()

    linhasarq.close()

    return linhas


def ler_tabelas(linhas):

    #procs[1]

    blocos = int(linhas[0])

    segmentos = int(linhas[1])

    tabela1=[]

    for lin in linhas[2:(segmentos+2)]:
        dados={}
        coluna=lin.split(', ')
        dados['arq']=coluna[0]
        dados['bl_inicio']=int(coluna[1])
        dados['bl_tam']=int(coluna[2].rstrip('\n'))
        tabela1=tabela1+[dados]

    return tabela1


def ler_tabs(linhas):

    tab = []

    segmentos = int(linhas[1])

    for lin in linhas[(segmentos+2):]:
        dados = {}
        coluna = lin.split(', ')
        dados['pid'] = int(coluna[0])
        dados['oper'] = coluna[1]
        dados['arq'] = coluna[2].rstrip('\n')
        if int(dados['oper']) == 0:
            dados['blocos']=coluna[3].rstrip('\n')
        tab = tab+[dados]
    return tab


def get_blocos(linhas):

    blocos = int(linhas[0])

    return blocos


def main(endereco, arquivo):
    linhas = ler_arquivo(endereco, arquivo)
    tabela = ler_tabelas(linhas)
    tab = ler_tabs(linhas)
    blocos = get_blocos(linhas)

    print(' ---------------- Inicializando Espaco de Memoria ---------------- ')
    bloco_memoria = gerenciador_memoria.criar_espaco_memoria(blocos)
    if not bloco_memoria:
        exit()

    print(' ---------------- Preenchendo espacos na Memmória ---------------- ')
    gerenciador_memoria.processar_operacoes_memoria(tabela)

    if gerenciador_memoria.verifica_espaco_memoria_disponivel(3):
        posicoes = gerenciador_memoria.get_espaco_memoria_disponivel(3)
        if posicoes != 0:
            gerenciador_memoria.escrever_bloco_memoria_em_lote(posicoes, 'A')
    else:
        print('Erro! Memoria insuficiente!')


    # print('Arquivos')
    # print(tabela)
    #
    # print('Operacoes')
    # print(tab)
    
    return tabela
