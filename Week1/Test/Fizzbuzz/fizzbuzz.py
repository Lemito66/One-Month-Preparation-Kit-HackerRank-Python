def fizzbuzz(number: int):
    list_of_numbers = []
    for i in range(1,number+1):
        if i % 3==0 and i % 5 ==0:
            list_of_numbers.append('FizzBuzz')
        elif i % 3==0:
            list_of_numbers.append('Fizz')
        elif i % 5==0:
            list_of_numbers.append('Buzz')
        else:
            list_of_numbers.append(i)
    return list_of_numbers

for i in fizzbuzz(100):
    print(i)