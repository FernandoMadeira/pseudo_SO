#leitor lista processos

#endereco ='C:\Users\Fernando Windows\Documents'
import os

if os.getcwd() != os.path.join('C:\\','Users','Fernando Windows','Documents'):
    os.chdir(os.path.join('C:\\','Users','Fernando Windows','Documents'))

arquivo = 'processes.txt'


lista_proc=open(arquivo)

procs=lista_proc.readlines()
#procs[1]

tabela=[]

for proc in procs:
    dados={}
    coluna=proc.split(', ')
    dados['pid']=len(tabela)
    dados['tempo_inic']=int(coluna[0])
    dados['prior']=int(coluna[1])
    dados['tempo_proc']=int(coluna[2])
    dados['blocos']=int(coluna[3])
    dados['cod_impr']=coluna[4]
    dados['req_scan']=coluna[5]
    dados['req_modem']=coluna[6]
    dados['cod_disco']=coluna[7]
    tabela=tabela+[dados]

print(tabela)

tempos_proc=[]

for item in tabela:
    tempos_proc=tempos_proc+[item['tempo_proc']]

print(tempos_proc)

tabela[1]['prior']
tabela[:]['prior']




import pprint

pprint.pprint(tempos_proc)

