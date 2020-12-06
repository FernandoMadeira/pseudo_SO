import gestor_filas


def status_processo(processo,processos,tempo):
    if processo == gestor_filas.filatempo(processos,tempo)[0]:
        return 'Em execução'
    elif processo in gestor_filas.filatempo(processos,tempo)[1:]:
        return 'Fila de pronto'
    elif processo['tempo_inic'] + processo['tempo_proc'] < int(tempo):
        return 'Processado'
    else:
        return 'Ainda não entrou na fila'


#def efetua_operacoes(proc,processos,t):



#def executa(processos):
#    t=0
#    while any(processos)
#    for proc in processos:
#        if status_processo(proc,processos,t) == 'Em execução':
#            efetua_operacoes(proc)
#    t=t+1



