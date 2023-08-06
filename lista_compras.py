# VARIÁVEIS
lista_compras_var = []

# FUNÇÕES
def VERIFICAR_TAMANHO_LETRA(minusc, maiusc, entrada):
    return entrada.lower() == minusc or entrada.upper() == maiusc

def lista_compras():
    if not lista_compras_var: 
        print('--SUA LISTA ESTÁ VAZIA--\n\n')
    else:
        print('LISTA DE COMPRAS\n')
        for indice, item in enumerate(lista_compras_var):
            print(f'{indice+1}: {item}')


    entrada_lista = input('\nVocê deseja adicionar item a lista? "S" ou  "N"->') # AÇÃO SE USUÁRIO DESEJA OU NÃO ADICIONAR ALGO A LISTA
    if VERIFICAR_TAMANHO_LETRA('s', 'S', entrada_lista):
        print('LISTA DE COMPRAS\n\n')
        for indice, item in enumerate(lista_compras_var):
            print(f'{indice+1}: {item}')

        INSERIR_COMPRAS()
    elif VERIFICAR_TAMANHO_LETRA('n', 'N', entrada_lista):
        main() # CHAMADA DA FUNÇÃO PRIMÁRIA PARA RECOMEÇAR A LÓGICA
    elif not lista_compras_var:
        print('LISTAS DE COMPRAS ESTÁ VAZIO\n')
        lista_compras()
    else:
        print('\nESCOLHA UMA OPÇÃO VÁLIDA\n')
        
def INSERIR_COMPRAS():
    i = len(lista_compras_var) + 1
    print('Para sair digite [sair, SAIR]')
    while True:
        adicionar_item_lista = input(f'{i}: ')
        if VERIFICAR_TAMANHO_LETRA('sair', 'SAIR', adicionar_item_lista):
            break
        if adicionar_item_lista == '':
            print('--A lista não pode ficar sem algum item--')
            continue
        else:
            lista_compras_var.append(adicionar_item_lista)

            i += 1

def DELETAR_COMPRAS():
    ...

def main():
    while True:
        entrada_in = input('L: Lista de compras \nI: Inserir item à lista de compras \n\
D: Apagar item da lista de compras \n-> ')
        nao_digito = not entrada_in.isdigit() # NÃO ACEITA SOMENTE NÚMEROS.
        
        if nao_digito and VERIFICAR_TAMANHO_LETRA('l', 'L', entrada_in):
            lista_compras()
        elif VERIFICAR_TAMANHO_LETRA('fechar', 'FECHAR', entrada_in):
            print('encerrando o programa')
            break
        else:
            ...
main()