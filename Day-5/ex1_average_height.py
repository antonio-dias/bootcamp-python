students_heights = input("Input a list of student heights ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])


count_students = len(students_heights)
sum_height = 0
for student in students_heights:
    sum_height += student

average_height = sum_height / count_students

print(round(average_height))