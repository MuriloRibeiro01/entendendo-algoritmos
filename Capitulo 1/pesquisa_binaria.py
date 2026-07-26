def pesquisa_binaria(lista, item):
    # baixo e alto acompanham a parte da lista que você está procurando
    baixo = 0
    alto = len(lista) - 1

    # enquanto ainda não conseguiu chegar a um único elemento...
    while baixo <= alto:
        # ... verifica o elemento central
        meio = (baixo + alto) // 2
        chute = lista[meio]
        # Acha o item!
        if chute == item:
            return meio

        # Chute muito alto
        if chute > item:
            alto = meio - 1
        # Chute muito baixo
        else:
            baixo = meio + 1
    # O item não existe
    return None

minha_lista = [1, 7, 12, 13, 21] # teste

print(pesquisa_binaria(minha_lista, 12)) # fica com índice 2
print(pesquisa_binaria(minha_lista, -1)) # Dá None, não existe na lsita.

# Numa lista de 128 elementos, qual seria o máximo de tentativas para achar um índice?
# R = 7
# E numa lista com o dobro de elementos?
# R = 14
