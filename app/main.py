import random
import time
from colorama import Fore, Style, init

init()

options = ('piedra', 'papel', 'tijera')
emojis = {'piedra': '🪨', 'papel': '📄', 'tijera': '✂️'}
rounds = 0
user_victories = 0
computer_victories = 0
attempts = 3

print(Fore.BLUE + "¡Bienvenido al juego de piedra, papel o tijera! 🎮" + Style.RESET_ALL)

while user_victories < 3 and computer_victories < 3 and attempts > 0:
  rounds += 1

  print(Fore.YELLOW + f'¡Ronda {rounds}!' + Style.RESET_ALL)
  user_choice = input('Elige piedra, papel o tijera: ')
  user_choice_lower = user_choice.lower()

  if not user_choice in options:
    attempts -= 1
    print(Fore.RED + f'Opción no válida. Te quedan {attempts} intentos.' + Style.RESET_ALL)
    continue

  computer_choice = 'piedra'
  # computer_choice = random.choice(options)

  print(f'Tú elegiste: {user_choice_lower} {emojis[user_choice_lower]}')
  time.sleep(2)
  print(f'Computadora eligió: {computer_choice} {emojis[computer_choice]}')

  if user_choice_lower == computer_choice:
    time.sleep(1)
    print(Fore.MAGENTA + '¡Empate! 🔄' + Style.RESET_ALL)
  elif user_choice_lower == 'piedra':
    time.sleep(1)
    if computer_choice == 'tijera':
      print(Fore.GREEN + '¡Ganaste esta ronda! 🎉' + Style.RESET_ALL)
      user_victories += 1
    else:
      print(Fore.RED + 'Perdiste esta ronda. 😢' + Style.RESET_ALL)
      computer_victories += 1
  elif user_choice_lower == 'papel':
    time.sleep(1)
    if computer_choice == 'piedra':
      print(Fore.GREEN + '¡Ganaste esta ronda! 🎉' + Style.RESET_ALL)
      user_victories += 1
    else:
      print(Fore.RED + 'Perdiste esta ronda. 😢' + Style.RESET_ALL)
      computer_victories += 1
  elif user_choice_lower == 'tijera':
    time.sleep(1)
    if computer_choice == 'papel':
      print(Fore.GREEN + '¡Ganaste esta ronda! 🎉' + Style.RESET_ALL)
      user_victories += 1
    else:
      print(Fore.RED + 'Perdiste esta ronda. 😢' + Style.RESET_ALL)
      computer_victories += 1

  print(f'Puntuación: Tú - {user_victories}, Computadora - {computer_victories}\n')

if user_victories == 3:
  print(Fore.GREEN + "¡Victoria! 🎉🎉🎉" + Style.RESET_ALL)
  # for i in range(10):
  #   print(Fore.GREEN + "🎉🎉🎉" + Style.RESET_ALL)
  #   time.sleep(0.3)
else:
  print(Fore.RED + "Derrota 😢" + Style.RESET_ALL)
  # for i in range(10):
  #   print(Fore.RED + "😢😢😢" + Style.RESET_ALL)
  #   time.sleep(0.3)

print(Fore.GREEN + "¡Gracias por jugar! 🎮" + Style.RESET_ALL)