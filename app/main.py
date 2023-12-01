'''
Challenge class 21
Transform the user_choise input to lowercase 
'''
user_choise = input('piedra, papel o tijera')
computer_choise = 'piedra'

user_choise_lower = user_choise.lower()

if user_choise_lower == computer_choise:
  print('Empate')
elif user_choise_lower == 'piedra':
  if computer_choise == 'tijera':
    print('Ganaste')
  else:
    print('Perdiste')
elif user_choise_lower == 'papel':
  if computer_choise == 'piedra':
    print('Ganaste')
  else:
    print('Perdiste')
elif user_choise_lower == 'tijera':
  if computer_choise == 'papel':
    print('Ganaste')
  else:
    print('Perdiste')
