memoria = []


def criar_espaco_memoria( memoria = memoria):
    print(' ---------- CRIANDO ESPACO DE MEMORIA! ---------- ')
    for i in range(256):
        memoria.append(0)
    print(' ---------- ESPACO DE MEMORIA CRIADO COM SUCESSO! ---------- ')

    return True


def deletar_memoria( posicao , memoria = memoria):

    memoria[posicao] = 0


def get_bloco_memoria_all( memoria = memoria):

    return memoria


def escrever_bloco_memoria(bl_inicio, bl_tam, arq,  memoria = memoria):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        memoria[posicao] = arq


def escrever_bloco_memoria_em_lote(posicoes, arq,  memoria = memoria):

    for posicao in posicoes:
        memoria[posicao] = arq


def verifica_espaco_memoria_disponivel(tam_bloco, processo_usuario, memoria = memoria):
    # Retorna True ou False caso tenha o tamanho de blocos disponiveis

    if processo_usuario:
        # remove os 64 primeiros blocos que estao reservados para processos em tempo real
        memoria_usuario = memoria[64:]
        blocos = [0]*tam_bloco
        blocos_disp = blocos in [memoria_usuario[i:i + tam_bloco] for i in range(len(memoria_usuario) - 1)]

    else:
        blocos = [0] * tam_bloco
        blocos_disp = blocos in [memoria[i:i + tam_bloco] for i in range(len(memoria) - 1)]

    return blocos_disp


def get_espaco_memoria_disponivel(tam_bloco, processo_usuario):

    espaco_disp = 0
    posicoes = []

    if processo_usuario:
        range_ini = 65
        range_fim = 1025
    else:
        range_ini = 0
        range_fim = 1025

    for posicao in range(range_ini, range_fim):

        if memoria[posicao] == 0 and espaco_disp != tam_bloco:
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

