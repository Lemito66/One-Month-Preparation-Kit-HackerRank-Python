def find_the_median(list_of_numbers:list):
    lista_ordenada = sorted(list_of_numbers)
    mediana = ((len(lista_ordenada)+1)//2)
    
    return lista_ordenada[mediana-1]


print(find_the_median([8,6,5,7,9]))

def metodo_burbuja(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                number_to_replace = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j+1]
                list_of_numbers[j+1] = number_to_replace
    return list_of_numbers

print(metodo_burbuja([8,6,5,7,9]))