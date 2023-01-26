def flippingBits(number):
    binary_numbers = []
    bi_numbers = []
    while number != 0:
        new_number = number//2
        number_binary = number%2
        binary_numbers.append(number_binary)
        if new_number <= 1:
            binary_numbers.append(new_number)
            break
        number = new_number
    for i in range(32-len(binary_numbers)):
        bi_numbers.append(0)
    return print_list(binary_numbers+bi_numbers)

def print_list(list_of_numbers:list):
    cadena = ''
    for i in list_of_numbers:
        cadena += str(i)
    return cadena[::-1]

#Esta es la solución
def flipping_bits(n: int) -> int:
    return (2**32-1)^n



print(flipping_bits(4294967286))
print(flipping_bits(4294967294))



