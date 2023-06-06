import random

def verifica(numSelect, numUser):
    if numUser > numSelect:
        print("Too high.")
    elif numUser < numSelect:
        print("Too low.")
    else:
        return True
    return False

def set_dificult(difficulty):
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    return attempts

def show_point(attempts):
    attempts -= 1
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    return attempts

def show_victory(number, attempts):
    print(f"You got it! The answer was {number} and left {attempts} attempts")

print("Welcome to the Number Guessing Game!")

continue_game = True
while continue_game:
    print("I'm thinking of a number between 1 and 100.")
    select_number = random.randint(0, 100)
    difficulty = input("Chose a difficulty, Type 'easy' or 'hard': ")

    attempts = set_dificult(difficulty)

    if attempts > 0:

        if verifica(select_number, int(input("Make a guess: "))):
            continue_game = False
            show_victory(select_number, attempts)
            break

        attempts = show_point(attempts)

        while attempts > 0 and continue_game:
            if verifica(select_number, int(input("Guess again: "))):
                continue_game = False
                show_victory(select_number, attempts)
                break

            attempts = show_point(attempts)

    else:
        print("The difficult is not possible")

