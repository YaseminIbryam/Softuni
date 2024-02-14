employees_happiness = list(map(int, input().split()))
factor = int(input())
employees_happiness_after_factor = list(map(lambda x: x * factor, employees_happiness))
average_employees_happiness = sum(employees_happiness_after_factor) / len(employees_happiness_after_factor)
happy_employees = list(filter(lambda x: x > average_employees_happiness, employees_happiness_after_factor))
if len(happy_employees) >= len(employees_happiness_after_factor) - len(happy_employees):
    print(f"Score: {len(happy_employees)}/{len(employees_happiness_after_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness_after_factor)}. Employees are not happy!")
