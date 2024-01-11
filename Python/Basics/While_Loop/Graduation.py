student_name = input()
current_class = 1
failed = 0
grade_sum = 0
is_excluded = False

while current_class < 13:
    grade = float(input())
    if grade < 4.00:
        failed += 1
        if failed > 1:
            is_excluded = True
            break
        continue
    grade_sum += grade
    current_class += 1
if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = grade_sum / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
