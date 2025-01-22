import os

restaurantes = [{'nome':'Ratatouille','Categoria':'Italiano','ativo':True},
                {'nome':'Sushi','Categoria':'japoneza','ativo':True},
                    {'nome':'mec','Categoria':'Fast Food','ativo':True}]



def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_sub_opcoes('Até mais!')

def voltar_menu():
    input('\nPressione ENTER para continuar...')
    main()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()

def exibir_sub_opcoes(texto):
    '''Função para exibir as sub-opções'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_restaurante():
    '''Função para cadastrar um restaurante

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adicionar um novo restaurante a lista de restaurantes

    '''
    exibir_sub_opcoes('Cadastrar Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome':nome_do_restaurante, 'Categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurantes():

    '''Função para listar os restaurantes'''

    exibir_sub_opcoes('Listar Restaurantes')
    print('*' * 60)
    print(f'Nome do Restaurante'.ljust(22) + '| Categoria |'.ljust(23) + '| Status |')
    print('*' * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)}| {categoria.ljust(20)} | {ativo}')

    voltar_menu()

def alternar_status_restaurante():
    '''Função para alternar o status do restaurante'''
    exibir_sub_opcoes('Alternar Status do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_menu()

def escolher_opcao():
    '''Função para escolher uma opção'''
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) 

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



finalizar_app()

def main():
    '''Função principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()  