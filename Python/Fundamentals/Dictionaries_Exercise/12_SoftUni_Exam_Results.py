exam_results = {}
submissions = {}


def submit(language):
    if language in submissions.keys():
        submissions[language] += 1
    else:
        submissions[language] = 1
    return submissions


def store(username, language, points):
    points = int(points)
    if username not in exam_results.keys():
        exam_results[username] = {"language": language, "points": points}
    else:
        if points > exam_results[username]["points"]:
            exam_results[username]["points"] = points

    return exam_results


def ban(username):
    if username in exam_results.keys():
        del exam_results[username]


while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split('-')
    if "banned" in command:
        ban(command[0])
    else:
        exam_results = store(*command)
        submissions = submit(command[1])

print("Results: ")
for usernames, data in exam_results.items():
    print(f"{usernames} | {data['points']}")
print("Submissions: ")
for languages, submissions in submissions.items():
    print(f"{languages} - {submissions}")
