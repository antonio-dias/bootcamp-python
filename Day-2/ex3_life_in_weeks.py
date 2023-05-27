age = input("What is your current age? ")

left_years = 90 - int(age)

days = int(left_years) * 365
weeks = int(left_years) * 52
months = int(left_years) * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')