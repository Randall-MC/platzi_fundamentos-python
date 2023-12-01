numbers = (1, 2, 3, 4, 1)
strings = ("one", "two", "three", "four", "five")

# print(type(numbers))
# print(type(numbers[0]))
print(f'Pocisión dónde se encuentra "1": {numbers.index(1)}')
print(f'Cuántas veces se repite "1": {numbers.count(1)}')

# Puedes transformar un tupla a una lista
list_numbers = list(numbers)
# print(type(list_numbers))
# print(type(list_numbers[0]))

list_numbers.append(5)
print(list_numbers)

# Transforma una lista a una tupla
tuple_numbers = tuple(list_numbers)
print(tuple_numbers)
