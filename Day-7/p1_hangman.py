word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      | 
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      | 
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      | 
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      | 
=========
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      | 
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
      | 
=========
''', '''
  +---+
  |   |
      |
      |
      |
      | 
=========
''', ]

import random
word = random.choice(word_list)

lives = 6
display = []
word_lenght = len(word)
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check guessed letter
    for position in range(word_lenght):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    print(f' '.join(display))

    if "_" not in display:
        end_of_game = True
        print('You win!')

    print(stages[lives])