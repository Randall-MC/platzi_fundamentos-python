text = 'Ella sabe programar en Python'

# Index
print(text[6])

# Find the last character of a string
# Way number one
text_size = len(text)
print(text[text_size - 1])
# Way number two
print(text[-1])

#Slicing
# 3 is the initial position
# 8 is the final position
print(text[3:8])

# Negative indexes
# -2 is the last character
# -3 is the second last character
print(text[-2:-3])

# When the initial position is not given, the default is 0
print(text[:7])

# Whne the final position is not given, the default is the end of the string
print(text[7:])

# When both position are not given, the result is whole string
print(text[:])

# You can use a third agument to define the step
print(text[::2])

# Negative step
print(text[::-1])
