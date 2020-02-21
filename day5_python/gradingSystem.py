#Title
print("#"*30)
print("Student Mark Grading Calculator")

#User Input
print("#"*30)
studentName = input("Enter Student Name: ")
math = int(input("Enter marks for Maths: "))
eng = int(input("Enter marks for English: "))
kisw = int(input("Enter marks for Kiswahili: "))
print("#"*50)

#Grading Function
def gradeMarks(score):
    if (score >= 80 and score <= 100):
        return "A"
    elif (score >= 60 and score < 80):
        return "B"
    elif (score >= 40 and score < 60):
        return "C"
    elif (score >= 0 and score < 40):
        return "D"
    else:
        return "Invalid Score"

#Grade Display
print("Maths Grade : {}".format(gradeMarks(math)))
print("English Grade : {}".format(gradeMarks(eng)))
print("Kiswahili Grade : {}".format(gradeMarks(kisw)))

#Marks Calculator
def totalMarks(math,eng,kisw):
    computedTotal = math + eng + kisw
    return computedTotal

studentMarks = int(totalMarks(math,eng,kisw))
print("Student Total Marks : {}".format(studentMarks))
print("#"*30)

average = totalMarks(math,eng,kisw) / 3

print("Average Grade: {}".format(gradeMarks(average)))
print("#"*30)