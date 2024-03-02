pair_of_rows = int(input())
students = {}
for row in range(pair_of_rows):
    name, grade = input(), float(input())
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]
for name, grade in students.items():
    average_grade = sum(grade)/len(grade)
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")