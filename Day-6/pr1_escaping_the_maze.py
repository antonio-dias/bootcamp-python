# Exercise using the Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Methods to not give error
def turn_left():
    print("Turn Left")

def move():
    print("Move")

def wall_in_front():
    print('Wall in front')

def at_goal():
    return False

def wall_on_right():
    print('Wall on right')

def front_is_clear():
    print('Front is clear')

# Code start from here
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()

    if not wall_on_right():
        turn_right()