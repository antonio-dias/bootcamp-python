print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_bill = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")

calculate_bill_with_percentage = (int(percentage_bill) / 100) * float(total_bill)

result_total = float(total_bill) + calculate_bill_with_percentage

result = result_total / int(total_people)

print(f'Each person should pay: ${round(result, 2)}')