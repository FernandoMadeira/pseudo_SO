disco = []


def criar_blocos_disco(blocos):
    print(' ---------- CRIANDO ESPACO EM DISCO! ---------- ')
    for i in range(blocos):
        disco.append([0])

    print(' ---------- ESPACO EM DISCO CRIADO COM SUCESSO! ---------- ')
    return True


def escrever_disco(posicao, palavra):

    disco[posicao] = palavra


def remover_processo_memoria(arq, pid, processo_usuario):

    for posicao in range(len(disco)):
        if processo_usuario:
            if disco[posicao][0] == arq and disco[posicao][1] == pid:
                disco[posicao] = [0]
        else:
            if disco[posicao][0] == arq and disco[posicao][1] == pid:

                disco[posicao] = [0]
    return True


def get_bloco_disco_all():

    return disco


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
        disco[posicao] = arq


def escrever_bloco_disco_em_lote(posicoes, arq):

    for posicao in posicoes:
        disco[posicao] = arq


def verifica_espaco_disco_disponivel(tam_bloco):

    blocos = [[0]]*tam_bloco
    blocos_disp = blocos in [disco[i:i + tam_bloco] for i in range(len(disco) - 1)]

    return blocos_disp


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
