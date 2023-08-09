# VARIÁVEIS
lista_compras_var = []

# FUNÇÕES
def verificar_tamanho_letra(minusc, maiusc, entrada):
    return entrada.lower() == minusc or entrada.upper() == maiusc

def saida_usuario():
    ...


def lista_compras():
    if not lista_compras_var: 
        print('--SUA LISTA ESTÁ VAZIA--\n\n')
    else:
        print('LISTA DE COMPRAS\n')
        for indice, item in enumerate(lista_compras_var):
            print(f'{indice+1}: {item}')

    entrada_lista = input('\nVocê deseja adicionar item a lista? [S/N]') # AÇÃO SE USUÁRIO DESEJA OU NÃO ADICIONAR ALGO A LISTA
    if verificar_tamanho_letra('s', 'S', entrada_lista):
        print('LISTA DE COMPRAS\n\n')
        for indice, item in enumerate(lista_compras_var):
            print(f'{indice+1}: {item}')

        inserir_compras()
    elif verificar_tamanho_letra('n', 'N', entrada_lista):
        main() # CHAMADA DA FUNÇÃO PRIMÁRIA PARA RECOMEÇAR A LÓGICA
    else:
        print('\nESCOLHA UMA OPÇÃO VÁLIDA\n')
        lista_compras()


def inserir_compras():
    i = len(lista_compras_var) + 1
    print('Para sair digite [sair]')
    while True:
        adicionar_item_lista = input(f'{i}: ')
        if verificar_tamanho_letra('sair', 'SAIR', adicionar_item_lista):
            return lista_compras() 
        elif not adicionar_item_lista:
            print('--A lista não pode ficar sem algum item--')
            continue
        else:
            lista_compras_var.append(adicionar_item_lista)

            i += 1


def deletar_item():
    if not lista_compras_var:
        print('--Sua lista de compras está vazio--')
        entrada_lista_2 = input('\nDeseja adicionar algo a lista? [S/N]')
        if verificar_tamanho_letra('s', 'S', entrada_lista_2):
            return inserir_compras()
        elif verificar_tamanho_letra('n', 'N', entrada_lista_2):
            return lista_compras()
        else:
            print('--Entrada inválida. Digite [S/N] para continuar--')
    else:
        for i, item in enumerate(lista_compras_var):
            print(f'{i+1}: {item}')

        while True:
            entrada_deletar = input('Digite o índice para deletar ou [S] para sair: ')
            
            if entrada_deletar.isdigit():
                try:
                    entrada_deletar = int(entrada_deletar)

                    del lista_compras_var[entrada_deletar - 1]

                except:
                    print('--Índice não existente--')
                    continue
                
                for i, item in enumerate(lista_compras_var):
                    print(f'{i+1}: {item}')

            elif verificar_tamanho_letra('s', 'S', entrada_deletar):
                return lista_compras()
            elif verificar_tamanho_letra('n', 'N', entrada_deletar):
                continue
            else:
                print('--Entrada inválida--')
                continue
            

def main():
    while True:
        entrada_in = input('L: Lista de compras \nI: Inserir item à lista de compras \n\
D: Apagar item da lista de compras \n-> ')
        
        if verificar_tamanho_letra('l', 'L', entrada_in): # LISTAR
            return lista_compras()
        elif verificar_tamanho_letra('i', 'I', entrada_in): # ADICIONAR
            return inserir_compras()
        elif verificar_tamanho_letra('d', 'D', entrada_in): # DELETAR
            return deletar_item()
        elif verificar_tamanho_letra('fechar', 'FECHAR', entrada_in):
            print('encerrando o programa')
            break
        else:
            print('--Entrada inválida--')
main()