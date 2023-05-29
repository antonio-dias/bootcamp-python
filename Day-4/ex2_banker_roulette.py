names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

option_select = random.random(0, (len(names) - 1))

print(f'{names[option_select]} is going to buy the meal today!')