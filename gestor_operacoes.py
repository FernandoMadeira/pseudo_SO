import os
import gerenciador_memoria
import gerenciador_arquivo


# Funcao utilizada para Ler os dados do Arquivo que contém as Operações
def ler_arquivo(endereco, arquivo):

    if os.getcwd() != os.path.join(endereco):
        os.chdir(os.path.join(endereco))

    linhasarq = open(arquivo)

    linhas = linhasarq.readlines()

    linhasarq.close()

    return linhas


# função lê as intruções referentes ao preenchimento do disco
def ler_operacoes_disco(linhas):

    #procs[1]

    blocos = int(linhas[0])

    segmentos = int(linhas[1])

    tabela1 = []

    for lin in linhas[2:(segmentos+2)]:
        dados = {}
        coluna = lin.split(', ')
        dados['arq'] = coluna[0].strip()
        dados['bl_inicio'] = int(coluna[1])
        dados['bl_tam'] = int(coluna[2].rstrip('\n'))
        tabela1=tabela1+[dados]

    return tabela1


# funcao responsável por ler as operações que o processo irá realizar
def ler_operacoes_processo(linhas):

    tab = []

    segmentos = int(linhas[1])

    for lin in linhas[(segmentos+2):]:
        dados = {}
        coluna = lin.split(', ')
        dados['pid'] = int(coluna[0])
        dados['oper'] = coluna[1].strip()
        dados['arq'] = coluna[2].rstrip('\n').strip()
        if int(dados['oper']) == 0:
            dados['blocos'] = int(coluna[3].rstrip('\n'))
        tab = tab+[dados]
    return tab


# retorna a quantidade de blocos de disco que serão criados
def get_blocos(linhas):

    blocos = int(linhas[0])

    return blocos


# Main responsável por executar as operacoes
def main(endereco, arquivo):
    linhas = ler_arquivo(endereco, arquivo)
    operacoes = ler_operacoes_disco(linhas)
    # operacors_processo = ler_operacoes_processo(linhas)
    blocos = get_blocos(linhas)

    print(' ---------------- Inicializando Memoria ---------------- ')
    blocos_memoria_ativo = gerenciador_memoria.criar_espaco_memoria()
    if not blocos_memoria_ativo:
        exit()

    print(' ---------------- Inicializando DISCO ---------------- ')
    bloco_disco = gerenciador_arquivo.criar_blocos_disco(blocos)
    if not bloco_disco:
        exit()

    print(' ---------------- Preenchendo espacos em Disco ---------------- ')
    gerenciador_arquivo.processar_operacoes_disco(operacoes)
    
    return operacoes
