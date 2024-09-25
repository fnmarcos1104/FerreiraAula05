import os 

os.system('cls')

# n = int(input('Insira um numero: '))

print('\n[1] Sacar \n[2] Extrato \[0] Sair: \n')
opcao = int(input('Resposta: '))

match opcao:
    case 1:
        print('Sacando...')
    case 2:
        print('Exibindo o extrato...')



