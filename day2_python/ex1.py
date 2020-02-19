#Function Modulus
def addwithR(x,y):
    sum = x + y
    return sum
print("The sum of 5 + 2 = ",  addwithR(5,2), "\n") 

#Function Modulus
def modRemainder(a,b):
    rem = a % b
    return rem
print("The modulus of 10/3 is = ", modRemainder(10,3), "\n")

#Print with format function
a = 10
b = 3
result = modRemainder(a,b)
print("The modulus of {} and {} is {}".format(a,b,result))