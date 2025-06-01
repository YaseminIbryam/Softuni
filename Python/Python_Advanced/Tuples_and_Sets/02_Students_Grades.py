
students_count = int(input())
students = {}
for student in range(students_count):
    student, grade = input().split()
    if student in students.keys():
        students[student] += (float(grade),)
    else:
        students[student] = (float(grade),)
for student, grades in students.items():
    average_grade = sum(students[student]) / len(students[student])

    print(f"{student} -> {' '.join(tuple(map(lambda x: f'{x:.2f}', grades)))} (avg: {average_grade:.2f})")