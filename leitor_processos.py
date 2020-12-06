#leitor lista processos

import os
import pprint

def ler_arquivo(endereco, arquivo):

    if os.getcwd() != os.path.join(endereco):
        os.chdir(os.path.join(endereco))

    lista_proc = open(arquivo)

    procs = lista_proc.readlines()

    return procs

def montar_tabela_processos(procs):

    #procs[1]

    tabela = []

    for proc in procs:
        dados = {}
        coluna = proc.split(', ')
        dados['pid'] = len(tabela)
        dados['tempo_inic'] = int(coluna[0])
        dados['prior'] = int(coluna[1])
        dados['tempo_proc'] = int(coluna[2])
        dados['blocos'] = int(coluna[3])
        dados['cod_impr'] = coluna[4]
        dados['req_scan'] = coluna[5]
        dados['req_modem'] = coluna[6]
        dados['cod_disco'] = coluna[7]
        tabela = tabela+[dados]
        # tabela[1]['prior']
        # tabela[:]['prior']



    return tabela

def tempos_processamento(tabela):

    tempos_proc = []

    for item in tabela:
        tempos_proc = tempos_proc+[item['tempo_proc']]

    return tempos_proc

def lista_atributo(tabela, campo):

    atributo = []

    for item in tabela:
        atributo = atributo + [item[campo]]

    return atributo


def main(endereco, arquivo):

    processos = ler_arquivo(endereco, arquivo)
    tabela_processos = montar_tabela_processos(processos)
    tempos_proc = tempos_processamento(tabela_processos)

    print(tabela_processos)
    print(tempos_proc)
    #pprint.pprint(tempos_proc)
