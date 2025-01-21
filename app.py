import os

restaurantes = ['pizza','Ratatouille','Sushi','Hamburguer']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Até logo!')

def voltar_menu():
    input('\nPressione ENTER para continuar...')
    main()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de Restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurantes():
    os.system('cls')
    print('Lista de Restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_menu()



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) 

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativando restaurante...')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



finalizar_app()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()  