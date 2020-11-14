#leitor lista operacoes

#endereco ='C:\Users\Fernando Windows\Documents'
import os

if os.getcwd() != os.path.join('C:\\','Users','Fernando Windows','Documents'):
    os.chdir(os.path.join('C:\\','Users','Fernando Windows','Documents'))

arquivo = 'files.txt'


linhasarq = open(arquivo)

linhas = linhasarq.readlines()
#procs[1]

blocos = int(linhas[0])

segmentos = int(linhas[1])



tabela=[]

for lin in linhas[2:(segmentos+2)]:
    dados={}
    coluna=lin.split(', ')
    dados['arq']=coluna[0]
    dados['bl_inicio']=int(coluna[1])
    dados['bl_tam']=int(coluna[2])
    tabela=tabela+[dados]

print(tabela)

tab=[]

for lin in linhas[(segmentos+2):]:
    dados={}
    coluna=lin.split(', ')
    dados['proc']=coluna[0]
    dados['oper']=coluna[1]
    dados['arq']=coluna[2]
    if int(dados['oper'])==0:
        dados['blocos']=coluna[3]
    tab=tab+[dados]

print(tab)



