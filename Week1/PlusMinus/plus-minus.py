def plus_minus(arr: list):
    list_of_numbers_negatives = []
    list_of_numbers_positives = []
    list_of_numbers_zeros = []
    for number in arr:
        if number < 0:
            list_of_numbers_negatives.append(number)
        elif number == 0:
            list_of_numbers_zeros.append(number)
        else:
            list_of_numbers_positives.append(number)
            
    return f'{(len(list_of_numbers_positives)/len(arr)):.6f} \n{(len(list_of_numbers_negatives)/len(arr)):.6f} \n{(len(list_of_numbers_zeros)/len(arr)):.6f}'

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plus_minus(arr))
