# 1 Variables and data types
name='Alice'
age=24
height=5.5
is_student=True
hobbies=['reading','running','coding']


print("Name:",name)
print("age:",age)
print("Height",height)
print("Student:",is_student)
print("Hobbies:",hobbies)

# 2 Conditional Statements

if age > 18:
    print(f"{name} is a adult")
else:
    print(f"{name} is a minor")

# 3. Loops
# For loop

print("hobbies")
for hobby in hobbies:
    print("-",hobby)


#while

count=0
while count < 3:
    print("Count is:",count)
    count += 1

# 4 functions

def greet_person(person_name):
    return f"Hello , {person_name}!"

greeting = greet_person(name)
print(greeting)

# 5. File operations
# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is basics file\n")
    file.write("It covers variables, loops, and file operations\n")

# Reading from a file

with open("example.txt", 'r') as file:
    content=file.read()
    print(content)


# 6. list Comprehenshions
numbers=[1,2,3,4,5]
squared_numbers = [x ** 2 for x in numbers]
print("Squared Numbers result:",squared_numbers)


# 7. Exception handling.
try:
    result=10/0
except ZeroDivisionError:
    print("Division by 0 is not allowed!!")


# 8 . Simple class and object

class person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def introduce(self):
        return f"My name is : {self.name} and my age is: {self.age}"

Person=person("Alicey",23)
print(Person)
print(Person.introduce())


# 9.Modules and Math..

import math
radius=7
area=math.pi * (radius ** 2)
print(f"Area of the circle with the radius {radius} : {area}")