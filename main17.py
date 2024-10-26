def product(numbers):
    product = 1
    for number in numbers:
        product = product * number
    return product


result = product([2, 3, 4])

print(result)