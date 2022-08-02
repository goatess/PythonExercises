from Student import Student

student = Student()

def addStudent(name, grade):
    student.setGrade(name, grade) 

def isCompetent():
    grade = student.grade
    if grade >= 5:
        print("Aprovado")
        return True
    else:
        print("Suspendido")
        return False
    
def printStudent():
    print(student.grade, student.name)
    print(isCompetent)
    
addStudent("Sara", 8)
print("Nombre del alumno/a:", student.name, "Nota:", student.grade)
isCompetent()
