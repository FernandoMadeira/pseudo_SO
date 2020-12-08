import gestor_filas
import gerenciador_arquivo
import gerenciador_memoria

opr_executadas = []

def processos_inicializados(processos):
    for proc in processos:
        proc['exec'] = 0
    return processos


def primeira_execucao(proc):
    proc['exec'] = 1

    return proc


def dispatcher(processos, operacoes):

    offset = 0
    for process in processos:

            print('Dispatcher => \n'
                  '       PID: '+str(process['pid'])+' \n'
                  '       offset: '+str(offset)+' \n'
                  '       blocks: ' + str(process['blocos']) + ' \n'
                  '       priority: ' + str(process['prior']) + ' \n'
                  '       time: ' + str(process['tempo_proc']) + ' \n'
                  '       printers: ' + str(process['cod_impr']) + ' \n'
                  '       scanners: ' + str(process['req_scan']) + ' \n'
                  '       modems: ' + str(process['req_modem']) + ' \n'
                  '       drivers: ' + str(process['cod_disco']) + ' \n')
            print('Processo '+str(process['pid'])+' =>')
            if process['blocos'] < 1024:
                print('P' + str(process['pid']) + ' STARTED')
                op_qtd = 0
                for op in operacoes:
                    if op['pid'] == process['pid']:
                        op_qtd = op_qtd+1
                        print('P'+str(process['pid'])+' instruction '+str(op_qtd))

                offset = offset + process['blocos']
                print('P'+str(process['pid'])+' return SIGINT')
                print(' \n')
            else:
                print('P'+str(process['pid'])+' Error => Memória insuficiente')
                print(' \n')




def operacoes_sem_processo(operacoes, instrucao):

    for opr in operacoes:
        if operacoes.index(opr) not in opr_executadas:
            print('Operação '+str(instrucao)+' => Falha')
            print('O Processo '+str(opr['pid'])+' não existe ou não foi criado por falta de memória!')
            instrucao = instrucao+1
            print(' ')



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


def efetua_operacoes(proc, processos, operacoes, t, instrucao):
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

                for opr in operacoes:
                    if opr['pid'] == proc['pid']:
                        instrucao = instrucao + 1
                        print('P'+str(proc['pid'])+' operação ' + str(instrucao))
                        if opr['oper'] == '1':
                            arq_removido = opr['arq']
                            gerenciador_arquivo.remover_arquivo_disco(arq_removido, opr['pid'], processo_usuario)    #remover_arquivo_disco(arq, pid, processo_usuario)  #criar essa função dentro do sistema de arquivos
                        elif opr['oper'] == '0':
                            arq_adicionado = opr['arq']
                            gerenciador_arquivo.adicionar_arquivo_disco(arq_adicionado, opr['pid'], opr['blocos'])      #criar essa função dentro do sistema de arquivos
                        else:
                            print('Operação desconhecida!')
                        print('')
                        index_opr = operacoes.index(opr)
                        opr_executadas.append(index_opr)

                # operacoes.pop(opr_index)
                # operacoes.remove(opr)
            else:
                index = processos.index(proc)
                processos[index]['tempo_proc'] = proc['tempo_proc'] - 1

            # REMOVER PROCESSO NA MEMÓRIA
            if proc['tempo_proc'] == 0:
                processos.remove(proc)
                gerenciador_memoria.remover_processo_memoria(proc['pid'])
        else:
            processos.remove(proc)

    return processos, operacoes, instrucao


def executa(processos, operacoes):

    processos = processos_inicializados(processos)
    t = 0
    instrucao = 0
    while len(processos) > 0:
        for proc in processos:
            processos, operacoes, instrucao = efetua_operacoes(proc, processos, operacoes, t, instrucao)

        t = t + 1
        # gatilho de seguranca
        if t > 1000:
            break
    # remove as operacoes já executadas
    operacoes_sem_processo(operacoes, instrucao+1)

    print(' ---------------- Mapa de ocupação do disco: ---------------- ')
    print(gerenciador_arquivo.get_bloco_disco_all())

    # print(' ---------------- Mapa de ocupação do disco arquivos e donos: ---------------- ')
    # print(gerenciador_arquivo.get_disco_posicao_processo_arquivo())

