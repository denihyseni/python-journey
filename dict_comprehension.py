import random
names = ["Alex","Beth",'Caroline','Dave','Eleanor','Freddie']
students_scores = {student : random.randint(1,100)  for student in names}
pass_students = {student : scores for (student,scores) in students_scores.items() if scores >= 50}
print(names)
print(students_scores)
print(pass_students)
