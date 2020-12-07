import gestor_filas
import gerenciador_arquivo
import gerenciador_memoria
import leitor_processos


def processos_inicializados(processos):
    for proc in processos:
        proc['exec'] = 0
    return processos


def primeira_execucao(proc):
    proc['exec'] = 1

    return proc


def status_processo(processo, processos, tempo):
    filaordenada = gestor_filas.filatempo(processos, tempo)

    if len(filaordenada) > 0:
        if filaordenada[0] == processo:
            return 'Em execução'
        elif processo in gestor_filas.filatempo(processos, tempo)[1:]:
            return 'Fila de pronto'
        elif processo['tempo_inic'] + processo['tempo_proc'] < int(tempo):
            return 'Processado'
        else:
            return 'Ainda não entrou na fila no tempo '
    else:
        return 'Lista Vazia'


def efetua_operacoes(proc, processos, operacoes, t):
    stprocessamento = status_processo(proc, processos, t)
    if stprocessamento == 'Em execução' and proc['tempo_proc'] > 0:
        processo_usuario = proc['prior'] in [1, 2, 3]
        if gerenciador_memoria.adicionar_processo_memoria(proc): #gerenciador_memoria.verifica_espaco_memoria_disponivel(64, False)
        #ADICIONAR PROCESSO NA MEMÓRIA
            if proc['exec'] == 0: #primeira_execucao(proc,processos):   #criar essa função
                proc = primeira_execucao(proc)
                index = processos.index(proc)
                processos[index] = proc

                index = processos.index(proc)
                processos[index]['tempo_proc'] = proc['tempo_proc'] - 1
                instrucao = 0
                for opr in operacoes:
                    if opr['pid'] == proc['pid']:
                        instrucao = instrucao + 1
                        print('P'+str(proc['pid'])+' instruction ' + str(instrucao))
                        if opr['oper'] == '1':
                            arq_removido = opr['arq']
                            gerenciador_arquivo.remover_arquivo_disco(arq_removido, opr['pid'], processo_usuario)    #remover_arquivo_disco(arq, pid, processo_usuario)  #criar essa função dentro do sistema de arquivos
                        elif opr['oper'] == '0':
                            arq_adicionado = opr['arq']
                            gerenciador_arquivo.adicionar_arquivo_disco(arq_adicionado, opr['pid'], opr['blocos'])      #criar essa função dentro do sistema de arquivos
                        else:
                            print('Operação desconhecida!')
            else:
                index = processos.index(proc)
                processos[index]['tempo_proc'] = proc['tempo_proc'] - 1

            # REMOVER PROCESSO NA MEMÓRIA
            if proc['tempo_proc'] == 0:
                processos.remove(proc)
                gerenciador_memoria.remover_processo_memoria(proc['pid'])

    return processos


def executa(processos, operacoes):

    processos = processos_inicializados(processos)
    t = 0
    while len(processos) > 0:
        for proc in processos:
            processos = efetua_operacoes(proc, processos, operacoes, t)

        t = t + 1
        # gatilho de seguranca
        if t > 100:
            break

    print(' --------- Mapa de ocupação do disco:x ----------------')
    print(gerenciador_arquivo.get_bloco_disco_all())


