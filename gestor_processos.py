import gestor_filas
import gerenciador_arquivo
import gerenciador_memoria


def status_processo(processo,processos,tempo):
    if processo == gestor_filas.filatempo(processos,tempo)[0]:
        return 'Em execução'
    elif processo in gestor_filas.filatempo(processos,tempo)[1:]:
        return 'Fila de pronto'
    elif processo['tempo_inic'] + processo['tempo_proc'] < int(tempo):
        return 'Processado'
    else:
        return 'Ainda não entrou na fila'


def efetua_operacoes(proc,processos,t):
    if tem_memoria(proc,processos,t):
        if status_processo(processo,processos,tempo) == 'Em execução' and proc['tempo_proc']>0:
            if primeira_execucao(proc,processos):   #criar essa função
                if proc['oper']=='1':
                    arq_removido = proc['arq']
                    remover_arquivo(arq_removido)      #criar essa função dentro do sistema de arquivos
                elif tab[j]['oper'] == '0':
                    arq_adicionado = tab[j]['arq']
                    adicionar_arquivo(arq_adicionado)      #criar essa função dentro do sistema de arquivos
                else:
                    print('Operação desconhecida!')
            else:
                proc['tempo_proc'] = proc['tempo_proc'] - 1




#def executa(processos):
#    t=0
#    while any(processos)
#    for proc in processos:
#        if status_processo(proc,processos,t) == 'Em execução':
#            efetua_operacoes(proc)
#    t=t+1



