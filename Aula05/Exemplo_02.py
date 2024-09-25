import os

os.system('cls')


print('\n[1] Manhã \n[2] Tarde \n[3] Noite')

turno = int(input('Informe o número do turno: '))

match turno:
    case 1:
        print('Manhã')
    case 2:
        print('Tarde')
    case 3:
        print('Noite')
    case _:
        print('Turno inválido')