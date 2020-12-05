import os
import pprint
# endereco ='C:\Users\Fernando Windows\Documents'
endereco = os.path.join('C:\\','Users','Fernando Windows','Documents','GitHub','pseudo_SO')
os.chdir(os.path.join('C:\\','Users','Fernando Windows','Documents','GitHub','pseudo_SO'))
os.getcwd()
arquivo = 'files.txt'
arquivo_processos = 'processes.txt'
#leitor lista processos
lista_proc = open(arquivo_processos)

procs = lista_proc.readlines()

tabela = []

for proc in procs:
    dados = {}
    coluna = proc.split(', ')
    dados['pid'] = len(tabela)
    dados['tempo_inic'] = int(coluna[0])
    dados['prior'] = int(coluna[1])
    dados['tempo_proc'] = int(coluna[2])
    dados['blocos'] = int(coluna[3])
    dados['cod_impr'] = coluna[4]
    dados['req_scan'] = coluna[5]
    dados['req_modem'] = coluna[6]
    dados['cod_disco'] = coluna[7].rstrip('\n')
    tabela = tabela+[dados]

tabela_processos = tabela

print(' ------------ Lendo Processos      ---------------- ')
#print(tabela_processos)
pprint.pprint(tabela_processos)


linhasarq = open(arquivo)
linhas = linhasarq.readlines()

blocos = int(linhas[0])
segmentos = int(linhas[1])

tabela1=[]

for lin in linhas[2:(segmentos+2)]:
    dados={}
    coluna=lin.split(', ')
    dados['arq']=coluna[0]
    dados['bl_inicio']=int(coluna[1])
    dados['bl_tam']=int(coluna[2].rstrip('\n'))
    tabela1=tabela1+[dados]

tab = []

segmentos = int(linhas[1])

for lin in linhas[(segmentos+2):]:
    dados = {}
    coluna = lin.split(', ')
    dados['pid'] = int(coluna[0])
    dados['oper'] = coluna[1]
    dados['arq'] = coluna[2].rstrip('\n')
    if int(dados['oper']) == 0:
        dados['blocos']=coluna[3].rstrip('\n')
    tab=tab+[dados]

print(' ------------ Lendo Arquivos       ---------------- ')
#print(tabela1)
pprint.pprint(tabela1)
print(' ------------ Lendo Operacoes      ---------------- ')
#print(tab)
pprint.pprint(tab)


#tempo real:
procstemporeal = []
for i in range(len(tabela_processos)):
    if tabela_processos[i]['prior']==0:
        procstemporeal = procstemporeal + [tabela_processos[i]]

#FIFO nao preemptivo tempo real:
procstemporealord = sorted(procstemporeal, key=lambda row:row['tempo_inic'])

#usuario:
procsusuario = []
for i in range(len(tabela_processos)):
    if tabela_processos[i]['prior'] in [1,2,3]:
        procsusuario.append(tabela_processos[i])

#problema prioridade
procsproblema = []
for i in range(len(tabela_processos)):
    if tabela_processos[i]['prior'] not in [0,1,2,3]:
        procsproblema.append(tabela_processos[i])

print(' ------------ Procs Tempo Real     ---------------- ')
pprint.pprint(procstemporeal)
print(' ------------ Procs Tempo Real Ordenado------------ ')
pprint.pprint(procstemporealord)
print(' ------------ Procs Usuario        ---------------- ')
pprint.pprint(procsusuario)


#gestor de arquivos

for j in range(len(tab)):
    if tab[j]['oper']=='1':
        arq_removido = tab[j]['arq']
        tabela2=[]
        for k in range(len(tabela1)):
            if tabela1[k]['arq'] not in [arq_removido]:
                tabela2.append(tabela1)
        tabela1=tabela2
    elif tab[j]['oper']=='0':
        arq_adicionado = tab[j]['arq']
        tamanho = tab[j]['blocos']
        tabela1.append([{'arq':arq_adicionado,'bl_inicio':777,'bl_tam':tamanho}])
        


print(' ------------ Lendo Arquivos       ---------------- ')
#print(tabela1)
pprint.pprint(tabela1)
