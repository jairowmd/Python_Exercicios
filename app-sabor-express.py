import os

# Lista armazena colecao de dados
restaurantes = ['jocas bar','pizza do Ze']

def exibir_nome_do_programa():
    print('sabor express\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. sair\n')

# para limpar a tela usamos os.system('cls') para windows
def finalizar_app():
    exibir_subtitulo('finalizando app')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opcao invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro para novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    # append coloca o nome do restaurante que foi definido la na lista para armazenamento
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcoes():

    # try e except servem para tentar uma execucao e se nao der certo tentar outra
    try:
    # por padrao uma variavel é do tipo string e numero é do tipo int, para converter para string usamos int()
        opcao_escolhida = int(input("Escolha uma opção: "))


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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