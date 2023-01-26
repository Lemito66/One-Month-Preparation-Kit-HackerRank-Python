def diagonal_difference(list_bidimentional: list):
    result = 0
    lista_diagonal_top = []
    lista_diagonal_bottom = []
    for i in range(len(list_bidimentional)):
        lista_diagonal_top.append(list_bidimentional[i][i])  # 0 0 + 1 1 + 2 2
        lista_diagonal_bottom.append(
            list_bidimentional[i][len(list_bidimentional)-1-i])  # 0 2 + 1 1 + 2 0
    result = abs(sum(lista_diagonal_top)-sum(lista_diagonal_bottom))
    return result


print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))