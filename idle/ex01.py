def mult(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult



print(mult([[1,8,-3],[4,-2,5]],2))