# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# mode = w - create or edit all file
# mode = a - add new information in the file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")