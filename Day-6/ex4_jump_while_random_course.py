# Exercise using the Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

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

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    while front_is_clear():
        if at_goal():
            break
        move()
    if not at_goal():
        jump