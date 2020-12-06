import gestor_filas
import gerenciador_arquivo
import gerenciador_memoria
import leitor_operacoes

def processos_inicializados(processos):
    for proc in processos:
        proc['exec'] = 0
    return processos

def primeira_execucao(proc):
    proc['exec'] = 1


def status_processo(processo,processos,tempo):
    if processo == gestor_filas.filatempo(processos,tempo)[0]:
        return 'Em execução'
    elif processo in gestor_filas.filatempo(processos,tempo)[1:]:
        return 'Fila de pronto'
    elif processo['tempo_inic'] + processo['tempo_proc'] < int(tempo):
        return 'Processado'
    else:
        return 'Ainda não entrou na fila'


def efetua_operacoes(proc,processos,operacoes,t):
    if leitor_operacoes.tem_memoria(proc,processos,t): #gerenciador_memoria.verifica_espaco_memoria_disponivel(64, False)
        #ADICIONAR PROCESSO NA MEMÓRIA
        processo_usuario == proc['prior'] in [1,2,3]
        if status_processo(processo,processos,tempo) == 'Em execução' and proc['tempo_proc']>0:
            if proc['exec'] == 0: #primeira_execucao(proc,processos):   #criar essa função
                primeira_execucao(proc)
                for opr in operacoes:
                    if opr['pid'] == proc['pid']:
                        if opr['oper']=='1':
                            arq_removido = opr['arq']
                            #remover_arquivo(arq_removido)
                            gerenciador_arquivo.remover_arquivo_disco(arq_removido, opr['pid'], processo_usuario)    #remover_arquivo_disco(arq, pid, processo_usuario)  #criar essa função dentro do sistema de arquivos
                        elif opr['oper'] == '0':
                            arq_adicionado = opr['arq']
                            gerenciador_arquivo.adicionar_arquivo_disco(arq_adicionado,opr['pid'],opr['blocos'])      #criar essa função dentro do sistema de arquivos
                        else:
                            print('Operação desconhecida!')
            else:
                proc['tempo_proc'] = proc['tempo_proc'] - 1
        #REMOVER PROCESSO NA MEMÓRIA




#def executa(processos):
#    t=0
#    while any(processos)
#    for proc in processos:
#        if status_processo(proc,processos,t) == 'Em execução':
#            efetua_operacoes(proc)
#    t=t+1



