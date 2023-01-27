def sock_merchant(list_of_numbers: list):
    pairs = 0
    diccionary_of_even_or_odd = {}
    for i in list_of_numbers:
        if i in diccionary_of_even_or_odd:
            diccionary_of_even_or_odd[i] += 1
        else:
            diccionary_of_even_or_odd[i] = 1
    for i in diccionary_of_even_or_odd:
        pairs += diccionary_of_even_or_odd[i] // 2
    return pairs


print(sock_merchant([4, 5 ,5 ,5, 6 ,6 ,4 ,1,4, 4 ,3 ,6 ,6 ,3, 6 ,1 ,4 ,5 ,5, 5]))
print(sock_merchant([1, 1, 1]))


