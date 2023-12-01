numbers = [1, 2, 3, 4, 5]
print(type(numbers))
print(numbers)

strings = ["Esto", "es", "una", "lista", "Python"]
print(strings)

types = ['Uno', 1, True]
print(types)

# Para obtener un valor de una lista, usamos el número de la pocisión del eleemento
print(numbers[0])
print(strings[2])
print(types[1])

# Puedes reemplazar el valor de un elmento dentro de una lista
numbers[0] = 6
print(numbers)

# También puedes seleccionar un rango de elementos de una lista
print(numbers[1:3])
print(strings[1:4])

# También puedes obtener el tamaño de una lista
print(len(numbers))

# Puedes usar el método 'in' para verificar si un elemento está en una lista
print(5 in numbers)
