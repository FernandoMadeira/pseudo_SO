import gestor_operacoes
import leitor_processos
import gestor_processos


def main():
    # caminho até a pasta com os arquivos
    #endereco = os.path.join('C:\\','Users','Fernando Windows','Documents','Github','pseudo_SO')
    endereco = '/Users/gabrieltomaz/Documents/UnB/1:2020/ISO/Trabalho/pseudo_SO'

    # arquivo de operacoes
    arquivo = 'files.txt'
    # arquivo de processos
    arquivo_processos = 'processes.txt'

    print(' ---------------- Lendo Processos ---------------- ')
    tabela_processos = leitor_processos.main(endereco, arquivo_processos)

    gestor_operacoes.main(endereco, arquivo)
    linhas = gestor_operacoes.ler_arquivo(endereco, arquivo)
    operacoes = gestor_operacoes.ler_operacoes_processo(linhas)

    print(' ---------------- Dispatcher      ---------------- ')
    gestor_processos.dispatcher(tabela_processos, operacoes)

    print(' ---------------- Execução ---------------- ')
    print('Sistema de arquivos =>')
    tabela_processos, operacoes = gestor_operacoes.processos_sem_memoria(tabela_processos, operacoes)
    gestor_processos.executa(tabela_processos, operacoes)

    print(' ---------------- FIM Execução ---------------- ')


if __name__ == "__main__":
    main()
