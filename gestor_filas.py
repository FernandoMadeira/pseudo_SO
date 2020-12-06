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

def temporealt(procs,prioridade,tempo):
    procstemporealt = []
    for i in range(len(procs)):
        if procs[i]['prior']<=prioridade and (procs[i]['tempo_inic']<=tempo and procs[i]['tempo_inic'] + procs[i]['tempo_proc'] > tempo):
            procstemporealt = procstemporealt + [procs[i]]
    return procstemporealt

#FIFO nao preemptivo tempo real:
def fifo(procs):
    procsord = sorted(procs, key=lambda row:row['tempo_inic'])
    return procsord 
#procstemporealord = sorted(procstemporeal, key=lambda row:row['tempo_inic'])

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
    print('------------ Processos Tempo Real Ordenados FIFO---')
    print(fifo(temporeal(procs)))
    print('------------ Processos Usuario       --------------')
    print(usuario(procs))
    print('------------ ----------------------- --------------')

def fila(procs):
    procsord1 = sorted(procs, key=lambda k: (k['tempo_inic'], k['prior']))
    return procsord1

def preempta(processo,processos,tempo):
    if processo['prior'] == 0:
        return False
    elif processo['prior'] == 1 and temporealt(processos,0,tempo) == []:
        return False
    elif processo['prior'] == 2 and temporealt(processos,1,tempo) == []:
        return False
    elif processo['prior'] == 3 and temporealt(processos,2,tempo) == []:
        return False
    else:
        return True

def filatempo(procs,tempo):
    filatempo = []
    for i in range(len(procs)):
        if (procs[i]['tempo_inic'] <= int(tempo)) and ((procs[i]['tempo_inic'] + procs[i]['tempo_proc']) > int(tempo)):
            filatempo.append(procs[i])
        if len(filatempo)>1000:
            print('Fila cheia!! 1000 processos!')
            filatempo.pop(1000)
            break
    filaordenada = fila(filatempo)
    #print(filaordenada)
    return filaordenada
