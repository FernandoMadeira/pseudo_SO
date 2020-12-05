#gestor de filas

#como saber que um processo é de usuário ou é de núcleo (tempo real)?


#fila de usuario

#entrada: dicionario chave-valor dos processos

#saida: lista ordenada dos processos prontos

#exemplo simples:
#entrada: lista de processos e suas prioridades
#saida: lista ordenada de processos

#print('insira a quantidade de processos')
#qtd=int(input())

#pids=[5,4,8,2,3]
#prioridade=[0,1,2,1,0]
#tempo_ini=[3,2,1,4,5]
#processos = {'n':nome,'p':prioridade}
#processos.keys()
#processos.values()

#prioridade1 = prioridade.sort()


#procs=[]
#for i in range(len(pids)):
#    procs.append({'pid':pids[i],'prioridade':prioridade[i],'tempo_inic':tempo_ini[i]})


#procsord = sorted(procs, key='prioridade')
#procsord = sorted(procs, key=lambda row:row['prioridade'])
#procsfiltrados
#0 in procs[1].values()
#procsfiltrados = {k: v for k,v in procs.items()}
#procsfiltrados = []

#procs[2]['prioridade']


#tempo real:
def temporeal(procs):
    procstemporeal = []
    for i in range(len(procs)):
        if procs[i]['prior']==0:
            procstemporeal = procstemporeal + [procs[i]]
    return procstemporeal

#usuario:
def usuario(procs):
    procsusuario = []
    for i in range(len(procs)):
        if procs[i]['prior'] in [1,2,3]:
            procsusuario.append(procs[i])
    return procsusuario

#problema prioridade
def problema(procs):
    procsproblema = []
    for i in range(len(procs)):
        if procs[i]['prior'] not in [0,1,2,3]:
            procsproblema.append(procs[i])
    return procsproblema

def imprime(procs):
    print('------------ Processos Tempo Real    --------------')
    print(temporeal(procs))
    print('------------ Processos Usuario       --------------')
    print(usuario(procs))

