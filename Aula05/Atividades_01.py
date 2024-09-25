import os

os.system('cls')


#  Atividade [1]   **Menu** - Elabore um programa que mostre o seguinte menu na tela: 
# Cadastro de Clientes 

# print('\n[0] Fim \n[1] Inclui \n[2] Altera \n[3] Exclui \n[4] Consulta')

# opc = int(input('Escolha uma das opções: '))

# match opc:
#     case 0:
#         print('Fim.')
#     case 1:
#         print('Inclui')
#     case 2:
#         print('Altera')
#     case 3:
#         print('Exclui')
#     case 4:
#         print('Consulta') 

# Fim [1]

# Atividade [2]     E os 10% do garçom? 

v = float(input('Digite o valor da conta: '))

g = v * 10 / 100

# ga = g / 100

vf = v + g

print(f'Taxa de serviço: R${g}')
print(f'Valor da conta: R${vf}')

# Fim [2]