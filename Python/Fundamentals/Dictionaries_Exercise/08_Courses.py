courses = {}
while True:
    command = input()
    if command == "end":
        for course, students in courses.items():
            print(f"{course}: {len(students)}")
            for student in students:
                print(f"-- {student}")
        break
    course, student = command.split(" : ")
    if course in courses:
        courses[course].append(student)
    else:
        courses[course] = [student]
