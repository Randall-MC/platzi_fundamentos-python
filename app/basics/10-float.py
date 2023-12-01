# Curiosidades con númericos flotantes
x = 3.3
y = 1.1 + 2.2

print(x)
print(type(x))
print(y)
print(type(y))
print(x == y)
print("--" * 10 + "\n")

y_str = format(y, '2g')
print(y_str)
print(type(y_str))
print(x == float(y_str))
print("--" * 10 + "\n")

y_round = round(1.1 + 2.2, 1)
print(y_round)
print(type(y_round))
print(y_round == x)
print("--" * 10 + "\n")

tolerance = 0.00001
print(abs(x - y) < tolerance)