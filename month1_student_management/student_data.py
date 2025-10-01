students = []

def isfloat(grade):
    try:
        float(grade)   # try to convert
        return True
    except ValueError:
        return False

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    while True:
        name = input("Enter your name: ")
        if name.isalpha() == True:
            name = name
            break
        else:
            print("Invalid name. Please enter a valid Name.")
        continue

    while True:
        age = input("Enter Your Age: ")
        if age.isdigit() == True:
            age = age
            break
        else:
            print("Enter a valid age")
        continue

    while True:
        grade = input("enter your grade: ")
        if isfloat(grade) == True:
            grade = grade
            break
        else:
            print("Invalid grade: Enter a valid grade")
            continue


    student_dict = {"name":name, "age":age, "grade":grade}

    students.append(student_dict)
    
    
    pass

def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    for student in students:
        print(f"Name: {student["name"]},  Age: {student["age"]}, Grade: {student["grade"]}")
        print("---------------------------------------")
    pass



def get_average_grade():
    
    grade = [float(student["grade"]) for student in students]
    len_grade = len(grade)
    sum_grade = sum(grade)

    average = sum_grade / len_grade
    print(average)
    return average
    """
    TODO: Return the average grade of all students.
    """
    pass