disco = []
disco_posicao_processo_arquivo = []


def criar_blocos_disco(blocos):
    print(' ---------- CRIANDO ESPACO EM DISCO! ---------- ')
    for i in range(blocos):
        disco.append([0])

    print(' ---------- ESPACO EM DISCO CRIADO COM SUCESSO! ---------- ')
    return True


def escrever_disco(posicao, palavra):

    disco[posicao] = palavra


def remover_arquivo_disco(arq, pid, processo_usuario):

    if (not processo_usuario) or (processo_usuario and verificar_arquivo_processo(arq, pid)):
        for posicao in range(len(disco)):
            if disco[posicao] == arq:
                disco[posicao] = [0]
    else:
        print('Erro de remoção! Arquivo não pertence ao Processo!')
    return True


#função ADICIONAR ARQUIVO
def adicionar_arquivo_disco(arq, pid, tamanho):
    if verifica_espaco_disco_disponivel(tamanho):
        posicoes = get_espaco_disco_disponivel(tamanho)
        if posicoes != 0:
            escrever_bloco_disco_em_lote(posicoes, arq, pid)
    else:
        print('Erro! Disco insuficiente!')



def get_bloco_disco_all():

    return disco


def get_disco_posicao_processo_arquivo():
    return disco_posicao_processo_arquivo


def verificar_disco(bl_inicio, bl_tam):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        if disco[posicao] != [0]:
            return False

    return True


def processar_operacoes_disco(operacoes):

    for opr in operacoes:
        if verificar_disco(opr['bl_inicio'], opr['bl_tam']):
            escrever_bloco_disco(opr['bl_inicio'], opr['bl_tam'], opr['arq'])
            print('Arquivo salvo')
        else:
            print('Erro! Espaço não disponivel')


def escrever_bloco_disco(bl_inicio, bl_tam, arq):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        disco[posicao] = [arq]


def escrever_bloco_disco_em_lote(posicoes, arq, pid, disco = disco):

    for posicao in posicoes:
        disco[posicao] = [arq]

    disco_posicao_processo_arquivo.append([arq, pid])


def verifica_espaco_disco_disponivel(tam_bloco):

    blocos = [[0]]*tam_bloco
    blocos_disp = blocos in [disco[i:i + tam_bloco] for i in range(len(disco) - 1)]

    return blocos_disp

def verificar_arquivo_processo(arq, pid):
    disp = [arq, pid] in disco_posicao_processo_arquivo

    return disp

def get_espaco_disco_disponivel(tam_bloco):

    espaco_disp = 0
    posicoes = []

    for posicao in range(len(disco)):

        if disco[posicao] == [0] and espaco_disp != tam_bloco:
            espaco_disp = espaco_disp+1
            posicoes.append(posicao)

        elif espaco_disp == tam_bloco:
            return posicoes
        else:
            posicoes = []
            espaco_disp = 0

    if espaco_disp == tam_bloco:
        return posicoes
    else:
        return 0
