''' Estructura de control if
if <condición>:
    <bloque de código>
elif <condición>:
    <bloque de código>
else:
    <bloque de código>
'''

# Evalua sin un número es par o inpar
numero = int(input('Ingrese un número: '))

if numero % 2 == 0:
  print(f"El número {numero} es par")
else:
  print(f"El número {numero} es impar")
