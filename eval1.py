students = {}

def add_student(student_id, name, student_class, grades):
   
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
        return

    students[student_id] = {
        'name': name,
        'class': student_class,
        'grades': grades
    }
    
   
    print(students)
def update_grades(student_id, new_grades):
   
    if student_id not in students:
        print(f"Student with ID {student_id} not found.")
        return

    students[student_id]['grades'] = new_grades
 
  

def calculate_average(student_id):
  
    if student_id not in students:
        print(f"Student with ID {student_id} not found.")
        return None

    grades = students[student_id]['grades']
    if not grades:
        print(f"wrong grade for student ID {student_id}.")
        return None

    average = sum(grades) / len(grades)
    return average


add_student('001', 'ROY', 'Math', [80, 85, 72])
add_student('002', 'ADAM', 'English', [68, 65, 90])
add_student('003', 'JOHN', 'Hindi', [75, 65, 97])

update_grades('001', [55, 80, 63])

print(f"Roy's average grade: {calculate_average('001')}")
print(f"Adam's average grade: {calculate_average('002')}")
print(students)

