person = {
    'name' : 'John',
    'lastname' : 'Doe',
    'age' : 30,
    'languages' : ['English', 'Spanish']
}

person['name'] = 'Jane'
person['age'] -= 5
person['languages'].append('French')

print(person)

del person['lastname']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
