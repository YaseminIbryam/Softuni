name_movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while name_movie != "Finish":
    available_seats = int(input())
    percent_full_salon = 0
    taken_seats = 0
    type_ticket = input()
    while type_ticket != "End":
        taken_seats += 1
        total_tickets += 1
        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == "kid":
            kids_tickets += 1
        if available_seats - taken_seats == 0:
            break
        type_ticket = input()
    percent_full_salon = taken_seats / available_seats
    print(f"{name_movie} - {percent_full_salon * 100:.2f}% full.")
    name_movie = input()
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets/total_tickets * 100:.2f}% kids tickets.")
