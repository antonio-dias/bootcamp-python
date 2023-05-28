height = float(input("enter yout height in m: "))
weight = float(input("enter yout weight in kg: "))

bmi = float(weight / height ** 2)
bmi_to_int = int(round(bmi, 0))

if bmi < 18.5:
    print(f"Your BMI is {bmi_to_int}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi_to_int}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi_to_int}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi_to_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_to_int}, you are clinically obese.")
