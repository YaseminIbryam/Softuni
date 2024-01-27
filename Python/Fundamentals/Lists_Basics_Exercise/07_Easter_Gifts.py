names_of_the_gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        gift = command[1]
        while gift in names_of_the_gifts:
            index = names_of_the_gifts.index(gift)
            names_of_the_gifts.insert(index, "None")
            names_of_the_gifts.remove(gift)
    elif "Required" in command:
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(names_of_the_gifts):
            names_of_the_gifts[index] = gift
    elif "JustInCase" in command:
        gift = command[1]
        names_of_the_gifts.pop()
        names_of_the_gifts.append(gift)
    command = input()
for i in range(names_of_the_gifts.count("None")):
    names_of_the_gifts.remove("None")
print(" ".join(names_of_the_gifts))



# names_of_gifts = input().split(" ")
#
#
# command = input()
# while command != "No Money":
#     command_type, *other_info = command.split()
#     if "OutOfStock" in command_type:
#         for i, name in enumerate(names_of_gifts):
#             if other_info[-1] == name:
#                 names_of_gifts[i] = "None"
#     elif "Required" in command_type:
#         length = len(names_of_gifts)
#         if length > int(other_info[-1]) >= 0:
#             names_of_gifts[int(other_info[-1])] = other_info[0]
#     elif "JustInCase" in command_type:
#         names_of_gifts[-1] = other_info[-1]
#     command = input()
#
# print(" ".join(x for x in names_of_gifts if x != "None"))
