import gestor_filas
import gerenciador_arquivo
import gerenciador_memoria
import leitor_processos
import pprint

# lista Global de Processos
lista_processos = []


# Funcao responsável por inicializar os processos
def criar_processos(endereco, arquivo_processos):
    print(' ---------- CRIANDO PROCESSOS! ---------- ')
    processos = leitor_processos.ler_arquivo(endereco, arquivo_processos)
    lista_processos = leitor_processos.montar_tabela_processos(processos)
    print('---Lista de Processos em formato de lista de dicionário---')
    print(lista_processos)
    print('---Lista de Processos em formato de tabela---')
    print(list(lista_processos[0].keys()))
    for proc in lista_processos:
        print(list(proc.values()))
    print('---Lista de Processos em formato de lista de dicionário com um campo por linha---')
    pprint.pprint(lista_processos)
    #print(tempos_proc)
    #pprint.pprint(tempos_proc)

    #print(' ---------- LISTA PROCESSOS CRIADA COM SUCESSO! ---------- ')

    return True

# Funcao responsável por retornar o estado atual da lista de processos
def get_lista_processos():
    return lista_processos

def processos_inicializados(processos):
    for proc in processos:
        proc['exec'] = 0
    return processos

def primeira_execucao(proc):
    proc['exec'] = 1


def status_processo(processo,processos,tempo):
    filaordenada = gestor_filas.filatempo(processos,tempo)
    if filaordenada[0] == processo:
        return 'Em execução'
    elif processo in gestor_filas.filatempo(processos,tempo)[1:]:
        return 'Fila de pronto'
    #elif processo['tempo_inic'] + processo['tempo_proc'] < int(tempo):
    elif processo['tempo_proc']==0:
        return 'Processado'
    else:
        return 'Ainda não entrou na fila'


def efetua_operacoes(proc,processos,operacoes,t):
    if status_processo(proc, processos, t) == 'Em execução' and proc['tempo_proc'] > 0:
        processo_usuario = proc['prior'] in [1, 2, 3]
        if gerenciador_memoria.adicionar_processo_memoria(proc,processos,t): #gerenciador_memoria.verifica_espaco_memoria_disponivel(64, False)
        #ADICIONAR PROCESSO NA MEMÓRIA
            if proc['exec'] == 0: #primeira_execucao(proc,processos):   #criar essa função
                primeira_execucao(proc)
                for opr in operacoes:
                    if opr['pid'] == proc['pid']:
                        if opr['oper'] == '1':
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
            gerenciador_memoria.remover_processo_memoria(proc['pid'])
            # REMOVER PROCESSO NA MEMÓRIA
            if proc['tempo_proc'] == 0:
                print('Processo '+str(proc['pid'])+' finalizado')
                processos.remove(proc)
            




def executa(processos,operacoes):
    t=1
    while processos != []:
        for proc in processos:
            efetua_operacoes(proc,processos,operacoes,t)
        t=t+1
    print('foram feitas '+str(t)+' iterações')



