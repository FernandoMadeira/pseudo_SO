memoria = []


def criar_espaco_memoria(blocos, memoria = memoria):
    print(' ---------- CRIANDO ESPACO DE MEMORIA! ---------- ')
    if blocos <= 1024:
        for i in range(blocos):
            memoria.append([0])

        print(' ---------- ESPACO DE MEMORIA CRIADO COM SUCESSO! ---------- ')
        return True
    else:
        print(' ---------- ESPACO DE MEMORIA MAIOR QUE O SUPORTADO! ---------- ')
        return False


def inicializar_espaco_memoria(segmentos):
    print(' ---------- INIALIZANDO ESPACOS DE MEMORIA! ---------- ')
    for posicao in range(segmentos):
        escrever_memoria(posicao, [1])

    print(' ---------- MEMORIA INICIALIZADA COM SUCESSO! ---------- ')
    return True


def escrever_memoria(posicao, palavra, memoria = memoria):

    memoria[posicao] = palavra


def deletar_memoria( posicao , memoria = memoria):

    memoria[posicao] = [0]


def get_bloco_memoria_all( memoria = memoria):

    return memoria


def verificar_memoria(bl_inicio, bl_tam, memoria = memoria):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        if memoria[posicao] != [0]:
            return False

    return True


def processar_operacoes_memoria(operacoes):

    for opr in operacoes:
        if verificar_memoria(opr['bl_inicio'], opr['bl_tam']):
            escrever_bloco_memoria(opr['bl_inicio'], opr['bl_tam'], opr['arq'])
            print('Arquivo salvo')
        else:
            print('Erro! Espaço não disponivel')


def escrever_bloco_memoria(bl_inicio, bl_tam, arq,  memoria = memoria):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        memoria[posicao] = arq


def escrever_bloco_memoria_em_lote(posicoes, arq,  memoria = memoria):

    for posicao in posicoes:
        memoria[posicao] = arq


def verifica_espaco_memoria_disponivel(tam_bloco, memoria = memoria):

    blocos = [[0]]*tam_bloco
    blocos_disp = blocos in [memoria[i:i + tam_bloco] for i in range(len(memoria) - 1)]

    return blocos_disp


def get_espaco_memoria_disponivel(tam_bloco):

    espaco_disp = 0
    posicoes = []

    for posicao in range(len(memoria)):

        if memoria[posicao] == [0] and espaco_disp != tam_bloco:
            espaco_disp = espaco_disp+1
            posicoes.append(posicao)

        elif espaco_disp == tam_bloco:
            print(' --- espaco encontrado ----- ')
            print(posicoes)
            return posicoes
        else:
            posicoes = []
            espaco_disp = 0

    if espaco_disp == tam_bloco:
        return posicoes
    else:
        return 0

