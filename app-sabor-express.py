import os

def exibir_nome_do_programa():
    print('sabor express\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. sair\n')

# para limpar a tela usamos os.system('cls') para windows
def finalizar_app():
    os.system('cls')
    print('finalizando app')


def opcao_invalida():
    print('opcao invalida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()



def escolher_opcoes():

    # try e except servem para tentar uma execucao e se nao der certo tentar outra
    try:
    # por padrao uma variavel é do tipo string e numero é do tipo int, para converter para string usamos int()
        opcao_escolhida = int(input("Escolha uma opção: "))


        if opcao_escolhida == 1:
            print('1. cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('2. Listar restaurante')
        elif opcao_escolhida == 3:
            print('3. Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()       

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()