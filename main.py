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
    print(gestor_filas.temporeal(tabela_processos))

    print('------------- Fila em cada tempo --------------------')
    for t in range(10):
        print('tempo '+str(t))
        print(gestor_filas.filatempo(tabela_processos,t))
    
    print('------------- Fila em cada tempo PID --------------------')
    for t in range(10):
        print('tempo '+str(t))
        print(leitor_processos.lista_atributo(gestor_filas.filatempo(tabela_processos,t),'pid'))

    print(' ---------------------- Lendo Operacoes ---------------------- ')
    leitor_operacoes.main(endereco, arquivo)

    print(' ---------------------- Blocos de memoria ---------------------- ')
    bloco_memoria = gerenciador_memoria.get_bloco_memoria_all()
    print(bloco_memoria)


if __name__ == "__main__":
    main()
