def create_letter(name):
    with open("./input/Letters/starting_letter.txt") as letter:
        new_letter = letter.read().replace("[name]", name)
        with open("./output/ReadyToSend/letter_for_" + name + ".txt", mode="w") as letters:
            letters.write(new_letter)

with open("./input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        create_letter(name.strip())