l = ['um', 'dois', 'três']

# 01 - PILHA

def pi(list,alt):
    if alt == '1':
        list.insert(0,input('Digite o valor que será inserido na pilha: '))
    elif alt == '0':
        list.pop(0)
    else: 
        print('Opção inválida.')
    
    return list

# 02 - FILA

def fi(list,alt):
    if alt == '1':
        list.append(input('Digite o valor que será inserido na fila: '))
    elif alt == '0':
        list.pop(0)
    else: 
        print('Opção inválida.')

    return list

# 03 - LISTA ENCADEADA

def li(list,alt):
    if alt == '1':
        list.insert(int(input('Digite o índice do elemento quer adicionar: ')),input('Digite o valor que será inserido na lista encadeada: '))
    elif alt == '0':
        list.pop(int(input('Digite o índice do elemento que quer remover: ')))
    else: 
        print('Opção inválida.')
    
    return list


escolha = 0
while escolha != 4:
    escolha = input(f'\n----------------------------------\n\
    Lista atual: {l}\nEscolha Como vai trabalhar com a lista:\n1: PILHA\n2: FILA\n3: LISTA ENCADEADA\nOUTRA TECLA: SAIR\n\nDigite sua opção: ')
    if escolha == '1':
        l = pi(l,input('\nREMOVER ÍTEM: DIGITE 0\nINSERIR ÍTEM: DIGITE 1\n\nDigite sua opção: '))
    elif escolha == '2':
        l = fi(l,input('\nREMOVER ÍTEM: DIGITE 0\nINSERIR ÍTEM: DIGITE 1\n\nDigite sua opção: '))
    elif escolha == '3':
        l = li(l,input('\nREMOVER ÍTEM: DIGITE 0\nINSERIR ÍTEM: DIGITE 1\n\nDigite sua opção: '))
    else:
        print('Finalizando Programa...')
        escolha = 4
