#User Input
print("#"*50)
studentName = input("Enter Student Name: ")
math = int(input("Enter marks for Maths: "))
eng = int(input("Enter marks for English: "))
kisw = int(input("Enter marks for Kiswahili: "))

def gradeMath(math):
    if (math >= 80):
        print("Maths Grade is A")
    elif (math >= 60 and math < 80):
        print("Maths Grade is B")
    elif (math >= 40 and math < 60):
        print("Maths Grade is C")
    else:
        print("Maths Grade is D")

gradeMath(math)

def gradeEng(eng):
    if (math >= 80):
        print("English Grade is A")
    elif (math >= 60 and math < 80):
        print("English Grade is B")
    elif (math >= 40 and math < 60):
        print("English Grade is C")
    else:
        print("English Grade is D")

gradeEng(eng)

def gradeKisw(kisw):
    if (kisw >= 80):
        print("Kiswahili Grade is A")
    elif (kisw >= 60 and kisw < 80):
        print("Kiswahili Grade is B")
    elif (kisw >= 40 and kisw < 60):
        print("Kiswahili Grade is C")
    else:
        print("Kiswahili Grade is D")

gradeKisw(kisw)

def totalMarks(math,eng,kisw):
    computedTotal = math + eng + kisw
    return computedTotal

studentMarks = int(totalMarks(math,eng,kisw))
print("Student Total Marks : {}".format(studentMarks))

average = totalMarks(math,eng,kisw) / 3

def gradeTotal(average):
    if (average >= 80 ):
        print("Average Grade is A")
    elif (average >= 60 and average < 80):
        print("Average Grade is B")
    elif (average >= 40 and average < 60):
        print("Average Grade is C")
    else:
        print("Average Grade is D")

gradeTotal(average)

print("#"*50)