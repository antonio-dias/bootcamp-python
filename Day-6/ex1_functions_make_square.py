# Exercise using the Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Methods to not give error
def turn_left():
    print("Turn Left")

def move():
    print("Move")

# Code start from here
def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
move()