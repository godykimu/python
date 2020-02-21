PI = 3.142

#Ask for User Input
print("#"*50)
print("Area and Parameter of Circle Calculator")
radius = int(input("Enter the radius of the Circle: "))

#Function Area
def areaCircle(radius):
    area = PI * radius * radius
    return area

def parameterCircle(radius):
    circumference = 2 * PI * radius
    return circumference

#Display Area and Circumference
print("The Area of the Circle is : {} and Circumference is {}".format(areaCircle(radius),parameterCircle(radius)))
