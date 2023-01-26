def miniMaxSum(arr:list):
    list_of_sums =[]
    for number in range(len(arr)):
        list_of_sums.append(sum(arr)-arr[number])
    return min_number(list_of_sums), max_number(list_of_sums)

def max_number(arr:list):
    max_number = float('-inf')
    for number in arr:
        if number > max_number:
            max_number = number
    return max_number

def min_number(arr:list):
    min_number = float('inf')
    for number in arr:
        if number < min_number:
            min_number = number
    return min_number

for i in miniMaxSum([1,2,3,4,5]):
    print(i, end=' ')
