'''
Clase 9
Calcula el promedio del presupuesto de 3 meses
Crea 3 variables que almacenen el presupuesto individual de cada mes
Crea 1 variable que almacene el promedio
'''

# Consider this snippet from ./05-numbers.py:
# Input
budget_january = float(input("Ingrese el presupuesto del mes de enero: "))
budget_february = float(input("Ingrese el presupuesto del mes de febrero: "))
budget_march = float(input("Ingrese el presupuesto del mes de marzo: "))

# Process
average = (budget_january + budget_february + budget_march) / 3
print(average)
