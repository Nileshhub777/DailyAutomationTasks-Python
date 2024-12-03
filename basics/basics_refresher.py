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
