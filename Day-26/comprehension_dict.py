names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

import random

students_score = {student:random.randint(1, 100) for student in names}

print(students_score)

passed_students = {student:score for (student, score) in students_score.items() if score >= 60}

print(passed_students)