#Importação de biblioteca
import os
from datetime import date

#entrada de daos
nome = input('Informe seu nome: ')
idade = int(input('informe sua idade: '))
data = f'{date.today().day}/{date.today().month}/{date.today().year}'

#limpa console
os.system('cls')

#Inicio do loop
while True:
    print(f'{'-'*30} CINE PYTHON {'-'*30}\n')
    print()
    print('Sala 1 - A volta do parafuso que não foi - 12 anos') 
    print('Sala 2 - A volta do parafuso que quase foi - Livre') 
    print('Sala 3 - A volta do parafuso que não quis ir - 18 anos') 
    print('Sala 4 - A volta do parafuso que foi - 16 anos') 
    print('Sala 5 - A volta do parafuso que foi e não voltou - 18 anos') 

    #Escolha do usuário
    sala = input('\nSala desejada: ')

    #limpa console
    os.system('cls')

    #verifica a sala escolhida
    match sala:
        case '1':
            idade_minima = 12
            filme = 'A volta do parafuso que não foi'
        case '2': 
            idade_minima = 0
            filme = 'A volta do parafuso que quase foi'
        case '3': 
            idade_minima = 18
            filme = 'A volta do parafuso que não quis ir'
        case '4': 
            idade_minima = 16
            filme = 'A volta do parafuso que foi'
        case '5': 
            idade_minima = 18
            filme = 'A volta do parafuso que foi e não voltou'
        case _:
            print('Sala inexistente, favor selecionar outra opção.')
            continue
    #Verificação da idade
    if idade >= idade_minima:
        #impresão do ingresso
        print(f'Ingresso impresso no dia: {data}.\n')
        print(f'Filme: {filme}.')
        print(f'Sala: {sala}.')
        print(f'Usuário: {nome}.')
        print('\nSucesso! Tenha um ótimo filme.')
        break
    else:
        print(f'{nome} Não possui a idade minima para o filme {filme}')
        print('Favor selecionar outro filme!')
        continue