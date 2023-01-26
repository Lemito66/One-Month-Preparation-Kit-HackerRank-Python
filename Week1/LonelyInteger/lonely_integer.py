def lonely_integer(list_of_numbers: list):
    list_of_repetitions = []
    for i in range(len(list_of_numbers)):
        count= 0
        for j in list_of_numbers:
            if list_of_numbers[i] == j: #1,2,3,4,3,2,1
                count += 1 
        list_of_repetitions.append(count)
    index = list_of_repetitions.index(min_number(list_of_repetitions))
    return list_of_numbers[index]

def min_number(arr:list):
    min_number = float('inf')
    for number in arr:
        if number < min_number:
            min_number = number
    return min_number

print(lonely_integer([1,2,3,4,3,2,1]))