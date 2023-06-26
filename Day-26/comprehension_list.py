numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

print(numbers)
print(new_numbers)

name = "Antonio"
letters_list = [letter for letter in name]

print(name)
print(letters_list)

list_range = [number * 2 for number in range(1, 5)]

print(list_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_long_names = [name.upper() for name in names if len(name) > 4]
print(upper_long_names)