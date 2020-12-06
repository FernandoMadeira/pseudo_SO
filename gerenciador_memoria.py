# lista Global Com a Memória
memoria = []


# Funcao responsável por inicializar a memória
def criar_espaco_memoria():
    print(' ---------- CRIANDO ESPACO DE MEMORIA! ---------- ')
    for i in range(1024):
        memoria.append(0)
    print(' ---------- ESPACO DE MEMORIA CRIADO COM SUCESSO! ---------- ')

    return True


# Funcao responsável por remover o processos da memória
def remover_processo_memoria(pid):

    for posicao in range(len(memoria)):
        if memoria[posicao] == pid:
            memoria[posicao] = 0


# Funcao responsável por retornar o estado atual da memoria
def get_bloco_memoria_all():

    return memoria


# Funcao responsável por escrever na mémoria
def escrever_bloco_memoria_em_lote(posicoes, pid):

    for posicao in posicoes:
        memoria[posicao] = pid


# Funcao retornar True ou False caso tenha o tamanho de blocos disponiveis
def verifica_espaco_memoria_disponivel(tam_bloco, processo_usuario):

    if processo_usuario:
        # remove os 64 primeiros blocos que estao reservados para processos em tempo real
        memoria_usuario = memoria[64:]
        blocos = [0]*tam_bloco
        blocos_disp = blocos in [memoria_usuario[i:i + tam_bloco] for i in range(len(memoria_usuario) - 1)]

    else:
        blocos = [0] * tam_bloco
        blocos_disp = blocos in [memoria[i:i + tam_bloco] for i in range(len(memoria) - 1)]

    return blocos_disp


# Funcao responsavel por retornar os espacoes de memoria disponivel
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


# Funcao responsavel por adcionar o processo na memoria
def adicionar_processo_memoria(proc,processos,t):
    processo_usuario = proc['prior'] in [1, 2, 3]

    if verifica_espaco_memoria_disponivel(proc['blocos'], processo_usuario):
        posicoes_mem = get_espaco_memoria_disponivel(proc['blocos'], processo_usuario)
        if posicoes_mem != 0:
            escrever_bloco_memoria_em_lote(posicoes_mem, '1')
            return True
        else:
            print('Erro! Memoria insuficiente!')
            return False
