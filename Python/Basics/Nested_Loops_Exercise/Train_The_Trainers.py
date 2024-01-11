number_of_jury = int(input())
command = input()
num_presentation = 0
sum_of_avg_grade = 0
while command != "Finish":
    sum_grade = 0
    name_presentation = command
    num_presentation += 1
    for jury in range(number_of_jury):
        grade = float(input())
        sum_grade += grade
    avg_grade = sum_grade / number_of_jury
    sum_of_avg_grade += avg_grade
    print(f"{name_presentation} - {avg_grade:.2f}.")
    command = input()
avg_grade_of_presentations = sum_of_avg_grade / num_presentation
print(f"Student's final assessment is {avg_grade_of_presentations:.2f}.")
