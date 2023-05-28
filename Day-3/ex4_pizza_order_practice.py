print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
pepperoni_price = 0

if size == 'S':
    bill += 15
    pepperoni_price = 2
elif size == 'M':
    bill += 20
    pepperoni_price += 3
elif size == 'L':
    bill += 25
    pepperoni_price = 3

if add_pepperoni == 'Y':
    bill += pepperoni_price

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')