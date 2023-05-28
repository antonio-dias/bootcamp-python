number = int(input("Which number do you want to check? "))

result_calc = number % 2

if (result_calc == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")