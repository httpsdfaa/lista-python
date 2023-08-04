 # VARIÁVEIS
lista_compras = []

# FUNÇÕES
def VERIFICAR_TAMANHO_LETRA(minusc, maiusc, entrada):
    return entrada.lower() == minusc or entrada.upper() == maiusc

def LISTA_COMPRAS():
    if lista_compras == []: 
        print('--SUA LISTA ESTÁ VAZIA--\n\n')
    else:
        print('LISTA DE COMPRAS\n')
        for indice, item in enumerate(lista_compras):
            print(f'{indice}: {item}')


    entrada_lista = input('\nVocê deseja adicionar item a lista? "S" ou  "N"->') # AÇÃO SE USUÁRIO DESEJA OU NÃO ADICIONAR ALGO A LISTA
    if VERIFICAR_TAMANHO_LETRA('s', 'S', entrada_lista):
        print('LISTA DE COMPRAS\n\n')
        INSERIR_COMPRAS()
    elif VERIFICAR_TAMANHO_LETRA('n', 'N', entrada_lista):
        main() # CHAMADA DA FUNÇÃO PRIMÁRIA PARA RECOMEÇAR A LÓGICA
    elif lista_compras == []:
        print('LISTAS DE COMPRAS ESTÁ VAZIO\n')
        LISTA_COMPRAS()
    else:
        print('\nESCOLHA UMA OPÇÃO VÁLIDA\n')
        
def INSERIR_COMPRAS():
    i = 1
    while True:
        adicionar_valor_lista = input(f'{i}: ')
        if VERIFICAR_TAMANHO_LETRA('sair', 'SAIR', adicionar_valor_lista):
            return LISTA_COMPRAS()
        else:
            lista_compras.append(adicionar_valor_lista)

            i += 1
            continue
def main():
    while True:
        entrada_in = input('L: Lista de compras \nI: Inserir item à lista de compras \n\
D: Apagar item da lista de compras \n-> ')
        nao_digito = not entrada_in.isdigit() # NÃO ACEITA SOMENTE NÚMEROS.
        
        if nao_digito and VERIFICAR_TAMANHO_LETRA('l', 'L', entrada_in):
            LISTA_COMPRAS()
        elif VERIFICAR_TAMANHO_LETRA('fechar', 'FECHAR', entrada_in):
            break
main()