#leitor lista operacoes

import os
import gerenciador_memoria
import gerenciador_arquivo


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

    tabela1 = []

    for lin in linhas[2:(segmentos+2)]:
        dados = {}
        coluna = lin.split(', ')
        dados['arq'] = coluna[0]
        dados['bl_inicio'] = int(coluna[1])
        dados['bl_tam'] = int(coluna[2].rstrip('\n'))
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


#fazer uma função ADICIONAR PROCESSO EM MEMÓRIA: ok
def adicionar_processo_memoria(proc,processos,t):
    processo_usuario = proc['prior'] in [1, 2, 3]

    if gerenciador_memoria.verifica_espaco_memoria_disponivel(proc['blocos'], processo_usuario):
        posicoes_mem = gerenciador_memoria.get_espaco_memoria_disponivel(proc['blocos'], processo_usuario)
        if posicoes_mem != 0:
            gerenciador_memoria.escrever_bloco_memoria_em_lote(posicoes_mem, '1')
            return True
        else:
            print('Erro! Memoria insuficiente!')
            return False


def main(endereco, arquivo):
    linhas = ler_arquivo(endereco, arquivo)
    tabela = ler_tabelas(linhas)
    tab = ler_tabs(linhas)
    blocos = get_blocos(linhas)

    print(' ---------------- Inicializando Memoria ---------------- ')
    blocos_memoria_ativo = gerenciador_memoria.criar_espaco_memoria()
    if not blocos_memoria_ativo:
        exit()

    #fazer uma função ADICIONAR PROCESSO EM MEMÓRIA ok
    # if gerenciador_memoria.verifica_espaco_memoria_disponivel(64, False):
    #     posicoes_mem = gerenciador_memoria.get_espaco_memoria_disponivel(64, False)
    #     if posicoes_mem != 0:
    #         gerenciador_memoria.escrever_bloco_memoria_em_lote(posicoes_mem, '1')
    #RETURN TRUE
    # else:
    #     print('Erro! Memoria insuficiente!')
    #RETURN FALSE

    print(' ---------------- Inicializando DISCO ---------------- ')
    bloco_disco = gerenciador_arquivo.criar_blocos_disco(blocos)
    if not bloco_disco:
        exit()

    print(' ---------------- Preenchendo espacos em Disco ---------------- ')
    gerenciador_arquivo.processar_operacoes_disco(tabela)

    #fazer uma função ADICIONAR ARQUIVO
#    if gerenciador_arquivo.verifica_espaco_disco_disponivel(3):
#        posicoes = gerenciador_arquivo.get_espaco_disco_disponivel(3)
#        if posicoes != 0:
#            pid = 1
#            gerenciador_arquivo.escrever_bloco_disco_em_lote(posicoes, 'A', pid)
#    else:
#        print('Erro! Disco insuficiente!')

#    print(' ---------------- Memoria ---------------- ')
#    memoria_atual = gerenciador_memoria.get_bloco_memoria_all()
#    print(memoria_atual)

    print(' ---------------- Disco ---------------- ')
    disco_atual = gerenciador_arquivo.get_bloco_disco_all()
    print(disco_atual)

    # print(' ---------------- Mapa de Arquivo Processo ---------------- ')
    # disco_atual = gerenciador_arquivo.get_disco_posicao_processo_arquivo()
    # print(disco_atual)
    #
    #gerenciador_arquivo.remover_processo_memoria('Z', 1, True)

    #print(' ---------------- Disco DELETE ---------------- ')
    #disco_atual = gerenciador_arquivo.get_bloco_disco_all()
    #print(disco_atual)

    # print('Arquivos')
    # print(tabela)
    #
    # print('Operacoes')
    # print(tab)
    
    return tabela
