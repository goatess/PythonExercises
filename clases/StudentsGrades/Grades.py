from clases.StudentsGrades.Student import Student

students = []

def addStudent(name, grade):
    students.append(Student(name, grade))   

def isCompetent(name):
    index = students.index(name)
    grade = students[index].grade
    if grade >= 5:
        return True
    else:
        return False
    
def printStudent(name):
    index = students.index(name)
    print(students[index])
    print(isCompetent)
    
addStudent("Sara", 8)
printStudent()
