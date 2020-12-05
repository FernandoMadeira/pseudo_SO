import leitor_operacoes
import leitor_processos

def main():
    # endereco ='C:\Users\Fernando Windows\Documents'
    endereco = '/Users/gabrieltomaz/Documents/UnB/1:2020/ISO/Trabalho/pseudo_SO'
    arquivo = 'files.txt'
    arquivo_processos = 'processes.txt'

    print(' ------------ Lendo Processos      ---------------- ')
    leitor_processos.main(endereco, arquivo_processos)
    print(' ------------ Lendo Operacoes      ---------------- ')
    leitor_operacoes.main(endereco, arquivo)


if __name__ == "__main__":
    main()