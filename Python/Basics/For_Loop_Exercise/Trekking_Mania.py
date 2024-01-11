number_of_groups = int(input())
people_Musalla = 0
people_Mont_Blanc = 0
people_Kilimanjaro = 0
people_K2 = 0
people_Everest = 0
for group in range(number_of_groups):
    number_of_people_in_group = int(input())
    if number_of_people_in_group <= 5:
        people_Musalla += number_of_people_in_group
    elif 6 <= number_of_people_in_group <= 12:
        people_Mont_Blanc += number_of_people_in_group
    elif 13 <= number_of_people_in_group <= 25:
        people_Kilimanjaro += number_of_people_in_group
    elif 26 <= number_of_people_in_group <= 40:
        people_K2 += number_of_people_in_group
    elif number_of_people_in_group >= 41:
        people_Everest += number_of_people_in_group
total_people = people_Musalla + people_Mont_Blanc + people_Kilimanjaro + people_K2 + people_Everest
percent_Musalla = people_Musalla / total_people * 100
percent_Mont_Blanc = people_Mont_Blanc / total_people * 100
percent_Kilimanjaro = people_Kilimanjaro / total_people * 100
percent_K2 = people_K2 / total_people * 100
percent_Everest = people_Everest / total_people * 100
print(f"{percent_Musalla:.2f}%\n{percent_Mont_Blanc:.2f}%\n{percent_Kilimanjaro:.2f}%")
print(f"{percent_K2:.2f}%\n{percent_Everest:.2f}%")
