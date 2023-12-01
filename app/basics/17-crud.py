# CRUD (Create, Read, Update, Delete)

numbers = [1, 2, 3, 4, 5]
print(numbers)

tasks = ['Estudiar', 'Hacer ejercicio', 'Hacer tarea']

# Actualizar el último elemento
numbers[-1] = 6
print(numbers)

# Agregar un elemento al final de la lista
numbers.append(7)
print(numbers)

# Agregar un elemento en una pocisión específica
numbers.insert(4, 5)
print(numbers)

# Puedes sumar listas
new_list = numbers + tasks
print(new_list)

# Obtener la pocisición de un elemento
print(new_list.index('Hacer ejercicio'))

# Remover un elemnto por su valor
new_list.remove('Hacer ejercicio')
print(new_list)

# Remover un elemento por su pocisión
new_list.pop(7)
print(new_list)

# Remover el último elemento
new_list.pop()

# Reemplazar un elemento de la lista por otro valor
new_list[-1] = 0  # reemplaza el último elemento
print(new_list)

# Voltear una lista
new_list.reverse()
print(new_list)

# Ordenar una lista
new_list.sort()
print(new_list)
