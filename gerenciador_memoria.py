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



