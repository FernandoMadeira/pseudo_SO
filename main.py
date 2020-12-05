import os
import leitor_operacoes
import leitor_processos
import gerenciador_memoria
import gestor_filas


def main():
    endereco = os.path.join('C:\\','Users','Fernando Windows','Documents','Github','pseudo_SO')
    #endereco = '/Users/gabrieltomaz/Documents/UnB/1:2020/ISO/Trabalho/pseudo_SO'
    arquivo = 'files.txt'
    arquivo_processos = 'processes.txt'

    print(' ------------ Lendo Processos      ---------------- ')
    processos = leitor_processos.ler_arquivo(endereco, arquivo_processos)
    tabela_processos = leitor_processos.montar_tabela_processos(processos)
    leitor_processos.main(endereco, arquivo_processos)


    gestor_filas.imprime(tabela_processos)
    #print(gestor_filas.temporeal(tabela_processos))

    print(' ------------ Lendo Operacoes      ---------------- ')
    operacoes = leitor_operacoes.main(endereco, arquivo)
    print(operacoes)

    print(' ------------ Inicializando Espaco de Memoria')
    bloco_memoria = gerenciador_memoria.criar_espaco_memoria()
    print(bloco_memoria)

    print(' ------------ Operacoes na memoria --------- ')
    gerenciador_memoria.processar_operacoes_memoria(operacoes)

    print(' ------------ Blocos de memoria --------- ')
    bloco_memoria = gerenciador_memoria.get_bloco_memoria_all()
    print(bloco_memoria)


if __name__ == "__main__":
    main()
