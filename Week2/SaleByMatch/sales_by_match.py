def metodo_burbuja(list_of_numbers: list):
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                number_to_replace = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j+1]
                list_of_numbers[j+1] = number_to_replace
    return list_of_numbers


def sock_merchant(list_of_numbers: list):
    count = 0
    lista_ordenada = metodo_burbuja(list_of_numbers)
    for i in range(0,len(lista_ordenada)-1,2):
        if lista_ordenada[i] == lista_ordenada[i+1]:
            count +=1
        """ elif lista_ordenada[i+1] == lista_ordenada[i+2]:
            count +=1 """
    return count

print(sock_merchant([10,20,20,10,10,30,50,10,20]))
print(sock_merchant([1,2,1,2,1,3,2]))
print(metodo_burbuja([4, 5 ,5 ,5, 6 ,6 ,4 ,1,4, 4 ,3 ,6 ,6 ,3, 6 ,1 ,4 ,5 ,5, 5]))
print(sock_merchant([4, 5 ,5 ,5, 6 ,6 ,4 ,1,4, 4 ,3 ,6 ,6 ,3, 6 ,1 ,4 ,5 ,5, 5]))
#print(metodo_burbuja([10,20,20,10,10,30,50,10,20]))


