import os

os.system('cls')


# [1]

# print('\n[1] Janeiro \n[2] Fevereiro \n[3] Março \n[4] Abril \n[5] Maio \n[6] Junho')

# mes = int(input('Escolha uma das opções: '))

# match mes:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case 4:
#         print('Abril')
#     case 5:
#         print('Maio')
#     case 6:
#         print('Junho')

# [2]

# print('\n Chinês \n Italiano \n Mexicano \n Vegetariano')

# r = input('Digite o tipo de restaurante deseja: ')

# match r:
#     case 'chines':
#         print('Comida chinesa')
#     case 'Italiano':
#         print('Pizza')
#     case 'Mexicano':
#         print('Burrito')
#     case 'Vegetariano':
#         print('Vegetais')
#     case _:
#         print('Tipo Inválido')


# [3]

print('\n[1] Adicionar item \n[2] Remover item \n[3] Listar itens \n[4] Sair')

opc = int(input('Escolha uma das opçoes: '))
v = 50


match opc:
    case 1:
        print('Adicionar item')
        ai = int(input('Quantos itens deseja adicionar: '))
        va = v + ai
        print(f'{ai} foram adicionados.')
        print(f'Total de itens: {va}.')
    case 2:
        print('Remover item')
        ri = int(input('Quantos itens deseja remover: '))
        vr = v - ri
        print(f'{ri} itens foram removidos.')
        print(f'Total de itens: {vr}.')
    case 3:
        print('Listar Itens')
        print(f'Total de itens: {v}')
    case 4:
        print('Operação finalizada.')
    case _:
        print('Invalida')
    









# v = int(input('Digite um valor: '))

# match v:
#     case 1:
#         print(f'Foi adicionado {v} item')
#     case 2:
#         print('Remover item')
#     case 3:
#         print('Listar Itens')
#     case 4:
#         print('Sair')