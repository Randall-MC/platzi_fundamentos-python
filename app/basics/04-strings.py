name = "Carlos"
last_name = "Mendoza"

full_name = name + " " + last_name
print(full_name)

quote = "I'm a programmer"
print(quote)

quote = '"I am a programer"'
print(quote)

quote = 'I\'m a programmer'
print(quote)

# format
template = "Hello, my name is {} {}"
print(template.format(name, last_name))

template = "Hello, my name is {} {}".format(name, last_name)
print(template)

template = f"Hello, my name is {name} {last_name}"
print(template)

# Class 8: Challenge
# Print a new template using three variables instead of two.

age = 35
template = f"Hello, my name is {name} {last_name} and I am {age} years old"
print(template)
