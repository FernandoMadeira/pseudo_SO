import leitor_operacoes
import leitor_processos
import gerenciador_memoria


def main():
    # endereco ='C:\Users\Fernando Windows\Documents'
    endereco = '/Users/gabrieltomaz/Documents/UnB/1:2020/ISO/Trabalho/pseudo_SO'
    arquivo = 'files.txt'
    arquivo_processos = 'processes.txt'

    print(' ------------ Lendo Processos      ---------------- ')
    leitor_processos.main(endereco, arquivo_processos)

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
