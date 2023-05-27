height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)
print(str(int(bmi)))

# Or
weight_as_float = float(weight)
height_as_float = float(height)

bmi = weight_as_float / height_as_float ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)