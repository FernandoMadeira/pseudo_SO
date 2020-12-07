# lista Global com o Disco
disco = []

# lista Global com processos e seus arquivos
disco_posicao_processo_arquivo = []


# Funcao responsável por inicializar o Disco
def criar_blocos_disco(blocos):
    #print(' ---------- CRIANDO ESPACO EM DISCO! ---------- ')
    for i in range(blocos):
        disco.append([0])

    #print(' ---------- ESPACO EM DISCO CRIADO COM SUCESSO! ---------- ')
    return True


# Funcao responsável remover um arquivo do Disco
def remover_arquivo_disco(arq, pid, processo_usuario):

    #if (not processo_usuario) or (processo_usuario and verificar_arquivo_processo(arq, pid)):
    for posicao in range(len(disco)):
        if disco[posicao] == [arq]:
            disco[posicao] = [0]
    print('O processo '+str(pid)+' deletou o arquivo '+arq)
    # else:
    #     print('Erro de remoção! Arquivo não pertence ao Processo!')
    return True


# Funcao responsável por adicionar um arquivo em disco
def adicionar_arquivo_disco(arq, pid, tamanho):
    if verifica_espaco_disco_disponivel(tamanho):
        posicoes = get_espaco_disco_disponivel(tamanho)
        print('O processo '+str(pid)+' criou o arquivo '+arq+' (blocos '+str(posicoes)+ ').')
        if posicoes != 0:
            escrever_bloco_disco_em_lote(posicoes, arq, pid)
    else:
        print('O processo '+str(pid)+' não pode criar o arquivo '+arq+' falta de espaço.')


# Funcao responsável por informar a situacao atual do disco
def get_bloco_disco_all():

    return disco


# Funcao responsável por informar a situacao dos processos e arquivos
def get_disco_posicao_processo_arquivo():
    return disco_posicao_processo_arquivo


# verifica se existe espaço disponivel em disco
def verificar_disco(bl_inicio, bl_tam):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        if disco[posicao] != [0]:
            return False

    return True


# Funcao responsável por processar as operacoes em disco
def processar_operacoes_disco(operacoes):

    for opr in operacoes:
        if verificar_disco(opr['bl_inicio'], opr['bl_tam']):
            escrever_bloco_disco(opr['bl_inicio'], opr['bl_tam'], opr['arq'])
        else:
            print('Erro! Espaço não disponivel')


# Funcao responsável por escrever no disco em blocos
def escrever_bloco_disco(bl_inicio, bl_tam, arq):

    for posicao in range(bl_inicio, bl_inicio+bl_tam):
        disco[posicao] = [arq]


# Funcao responsável por escrever arquivos no disco
def escrever_bloco_disco_em_lote(posicoes, arq, pid):

    for posicao in posicoes:
        disco[posicao] = [arq]

    disco_posicao_processo_arquivo.append([arq, pid])


# verifica se existe espaço disponivel em disco
def verifica_espaco_disco_disponivel(tam_bloco):

    blocos = [[0]]*int(tam_bloco)
    blocos_disp = blocos in [disco[i:i + tam_bloco] for i in range(len(disco) - 1)]

    return blocos_disp


# Verifica se o processo de usuario é dono do arquivo em disco
def verificar_arquivo_processo(arq, pid):
    disp = [arq, pid] in disco_posicao_processo_arquivo

    return disp


# Funcao responsável por retornar os espaços disponiveis em disco
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
