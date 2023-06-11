# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("#f33")
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

list_names = ["Pikachu", "Squirtle", "Charmander"]
list_types = ["Electric", "Water", "Fire"]
table.add_column("Pokemon Name", list_names)
table.add_column("Type", list_types)

table.align = 'l'
print(table.align)

print(table)