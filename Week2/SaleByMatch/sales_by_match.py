def sock_merchant(list_of_numbers: list):
    pairs = 0
    dictionary_of_even_or_odds = {}
    for number in list_of_numbers:
        if number in dictionary_of_even_or_odds:
            dictionary_of_even_or_odds[number] +=1
        else:
            dictionary_of_even_or_odds[number] = 1
    for i in dictionary_of_even_or_odds:
        pairs += dictionary_of_even_or_odds[i] // 2
    return pairs


print(sock_merchant([4, 5 ,5 ,5, 6 ,6 ,4 ,1,4, 4 ,3 ,6 ,6 ,3, 6 ,1 ,4 ,5 ,5, 5]))
print(sock_merchant([1, 1, 1]))


