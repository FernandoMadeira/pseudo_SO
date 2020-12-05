memoria = []


def criar_espaco_memoria(memoria = memoria):

    for i in range(12):
        memoria.append([0])

    return memoria


def escrever_memoria(posicao, palavra , memoria = memoria):

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
        print('------- opr ----- ')
        print(opr)
        if verificar_memoria(opr['bl_inicio'], opr['bl_tam']):
            escrever_bloco_memoria(opr['bl_inicio'], opr['bl_tam'], opr['arq'])
            print('Arquivo salvo')
        else:
            print('Erro! Espaço não disponivel')


def escrever_bloco_memoria(bl_inicio, bl_tam, arq,  memoria = memoria):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        memoria[posicao] = arq



