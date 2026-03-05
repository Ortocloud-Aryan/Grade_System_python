student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores: 
    if 100 >= student_scores[key] >= 90:
        student_grades[key] = 'O' #Outstanding 

    elif 90 > student_scores[key] >= 80 :
        student_grades[key] = 'A+' #Above Average 
    
    elif 80 > student_scores[key] > 60:
        student_grades[key] = 'A' #Average
    
    elif student_scores[key] <= 60:
        student_grades[key] = 'B' #below Average
 

print(student_grades)