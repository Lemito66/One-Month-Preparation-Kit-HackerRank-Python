def find_the_median(list_of_numbers:list):
    lista_ordenada = sorted(list_of_numbers)
    mediana = ((len(lista_ordenada)+1)//2)
    
    return lista_ordenada[mediana-1]


print(find_the_median([8,6,5,7,9]))