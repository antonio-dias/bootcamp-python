rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors \n"))

cpu_choice = random.randint(0, 2)

print("Computer Chose: ")
print(options[cpu_choice])

if user_choice == 0 and cpu_choice == 2:
    print('You win!')
elif user_choice == 1 and cpu_choice == 0:
    print('You win!')
elif user_choice == 2 and cpu_choice == 1:
    print('You win!')

elif cpu_choice == 0 and user_choice == 2:
    print('You win!')
elif cpu_choice == 1 and user_choice == 0:
    print('You win!')
elif cpu_choice == 2 and user_choice == 1:
    print('You win!')

else:
    print("It's a draw")