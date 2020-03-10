courses = ['Maths', 'English', 'Science']
courses_2 = ['History', 'Geography']

courses.extend(courses_2)
courses.sort(reverse=False)

for index, course, in enumerate(courses, start = 1):
    print(index,':', course)

#Printing list using join
mystr = ', '.join(courses)
print(mystr)

#Tuple are Immutable
mytuple = ('Mike', 'Kim', 'George')
print(mytuple)