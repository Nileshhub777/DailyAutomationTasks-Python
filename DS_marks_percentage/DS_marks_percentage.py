students = [
    {"name": "Alice", "scores": [85, 92, 78, 88, 91,98]},  # Student 1
    {"name": "Bobby", "scores": [75, 80, 70, 85, 90,89]},    # Student 2
    {"name": "charmy", "scores": [95, 88, 84, 92, 85,87]}  # Student 3
]

def calculate_scores_and_percentage(students):
    for student in students:
        total_scores= sum(student["scores"])
        percentage=(total_scores/500) * 100
        student["total_scores"]=total_scores
        student["percentage"]=percentage

calculate_scores_and_percentage(students)

for student in students:
    print(student)
    print(f"Name: {student['name']}")
    print(f"Total score: {student['total_scores']}")
    print(f"Percentage score: {student['percentage']}")