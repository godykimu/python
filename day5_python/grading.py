# A Program to Grade Students Marks
print('#'*60)

studentName = input("Enter Student Name: ")
studentRegNo = input("Enter Student Registration Number: ")
math = int(input("Enter Maths Marks: "))
eng = int(input("Enter English Marks: "))
swa = int(input("Enter Swahili Marks: "))

print('#'*60)

# Function to Grade Score
def gradeMark(score):
    if (score >= 70 and score <= 100):
        return 'A'
    elif (score >= 60 and score < 70):
        return 'B'
    elif  (score >= 50 and score < 60):
        return 'C'
    elif (score >= 40 and score < 50):
        return 'D'
    elif (score >= 0 and score < 40):
        return 'E'
    else:
        return 'Invalid Marks'

# Display Grade per Subject
print('Student Name: {}'.format(studentName))
print('Student Reg No: {}'.format(studentRegNo))
print('Maths Grade: {}'.format(gradeMark(math)))
print('English Grade: {}'.format(gradeMark(eng)))
print('Swahili Grade: {}'.format(gradeMark(swa)))

# Function to Calculate total Marks
def totalMarks(num1,num2,num3):
    return num1 + num2 + num3

print('#'*60)

print('Total Marks : {}'.format(totalMarks(math,eng,swa)))

# Function to Calculate Average of Three Numbers
def average (avg):
    return int(avg/3)

print('Average Marks: {}'.format(average(totalMarks(math,eng,swa))))
print('Average Grade: {}'.format(gradeMark(average(totalMarks(math,eng,swa)))))

print('#'*60)