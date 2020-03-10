#Lists
courses = ['Maths','English','Swahili','History','CRE']
print(courses)
print(courses[1])
print(courses[0:2])
print(courses[2:])
print(courses[:2])
print(len(courses))

#List insertion
courses_2 = ['Science', 'Geography']

#Not effective insertion method, rather use extend function
# courses.insert(0 , courses_2)
courses.extend(courses_2)
print(courses)

#use of sorting to insert
courses.sort()
print(courses)

courses.reverse()
print(courses)

#Find index of list item
print(courses.index('Science'))

#check whether item exists in a list
print('Art' in courses)
print('Maths' in courses)

#print courses
for item in courses:
    print(item)