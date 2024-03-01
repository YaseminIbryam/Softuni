students = []
while True:
    course = input()
    if ':' not in course:
        for student in students:
            course = course.replace("_", " ")
            if student['course'] == course:
                print(f"{student['name']} - {student['ID']}")
        break
    course = course.split(':')
    name = course[0]
    ID = course[1]
    course = course[2]
    students.append({"name": name, "ID": ID, "course": course})
