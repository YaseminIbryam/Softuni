numbers = [int(i) for i in input().split()]
command = input().split()

while command[0] != "end":
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[0:int(command[1])])
            else:
                print(odd[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[-int(command[1]):])
            else:
                print(odd[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)





# def valid_index(sequence: list, index: int):
#     return 0 <= index < len(sequence)
#
#
# def invalid_count(sequence: list, count: int):
#     return count > len(sequence)
#
#
# def get_even_or_odd_elements(sequence: list, type: str):
#     if type == "odd":
#         return [x for x in sequence if x % 2 == 1]
#
#     return [x for x in sequence if x % 2 == 0]
#
#
# def exchange(sequence: list, index: int):
#     if not valid_index(sequence, index):
#         print("Invalid index")
#         return sequence
#
#     return sequence[index + 1:] + sequence[:index + 1]
#
#
# def max_index(sequence: list, even_odd: str):
#     max_num = get_even_or_odd_elements(sequence, even_odd)
#
#     if max_num:
#         number = max(max_num)
#         print(len(sequence) - sequence[::-1].index(number) - 1)
#
#     else:
#         print("No matches")
#
#     return sequence
#
# def min_index(sequence: list, even_odd: str):
#     min_num = get_even_or_odd_elements(sequence, even_odd)
#
#     if min_num:
#         number = min(min_num)
#         print(len(sequence) - sequence[::-1].index(number) - 1)
#
#     else:
#         print("No matches")
#
#     return sequence
#
#
# def first_count(sequence: list, count: int, even_odd: str):
#     if invalid_count(sequence, count):
#         print("Invalid count")
#         return sequence
#
#     print(get_even_or_odd_elements(sequence, even_odd)[:count])
#
#     return sequence
#
#
# def last_count(sequence: list, count: int, even_odd: str):
#     if invalid_count(sequence, count):
#         print("Invalid count")
#         return sequence
#
#     print(get_even_or_odd_elements(sequence, even_odd)[-count:])
#
#     return sequence
#
#
# def main(sequence: list, commands: dict):
#     command = input()
#     while command != "end":
#         operation, *info = [x if x.isalpha() else int(x) for x in command.split()]
#
#         sequence = commands[operation](sequence, *info)
#
#         command = input()
#
#     return sequence
#
#
#
# numbers = [int(x) for x in input().split()]
#
# operations = {
#     "exchange": exchange,
#     "max": max_index,
#     "min": min_index,
#     "first": first_count,
#     "last": last_count,
# }
#
#
# print(main(numbers, operations))


# MINE
# integers = list(map(int, input().split()))
# command = input().split()
#
# while command[0] != "end":
#     even = [number for number in integers if number % 2 == 0]
#     odd = [number for number in integers if number % 2 != 0]
#
#     if command[0] == "exchange":
#         stop_index = int(command[1])
#         if stop_index >= len(integers) or stop_index < 0:
#             print("Invalid index")
#         else:
#             integers = integers[stop_index + 1:] + integers[:stop_index + 1]
#     elif command[0] == "max":
#         if command[1] == "even":
#             if len(even) > 0:
#                 max_element = max(even)
#                 max_element_index_reversed = integers[::-1].index(max_element)
#                 print(len(integers) - max_element_index_reversed - 1)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if len(odd) > 0:
#                 max_element = max(odd)
#                 max_element_index_reversed = integers[::-1].index(max_element)
#                 print(len(integers) - max_element_index_reversed - 1)
#             else:
#                 print("No matches")
#     elif command[0] == "min":
#         if command[1] == "even":
#             if len(even) > 0:
#                 min_element = min(even)
#                 min_element_index_reversed = integers[::-1].index(min_element)
#                 print(len(integers) - min_element_index_reversed - 1)
#             else:
#                 print("No matches")
#         elif command[1] == "odd":
#             if len(odd) > 0:
#                 min_element = min(odd)
#                 min_element_index_reversed = integers[::-1].index(min_element)
#                 print(len(integers) - min_element_index_reversed - 1)
#             else:
#                 print("No matches")
#     elif command[0] == "first":
#         count = int(command[1])
#         if 0 > count or count > len(integers):
#             print("Invalid count")
#         else:
#             indexes = []
#             if command[2] == "even":
#                 for index in range(count):
#                     if len(even) == index:
#                         break
#                     indexes.append(even[index])
#             elif command[2] == "odd":
#                 for index in range(count):
#                     if len(odd) == index:
#                         break
#                     indexes.append(odd[index])
#             print(indexes)
#     elif command[0] == "last":
#
#         count = int(command[1])
#         if 0 > count or count > len(integers):
#             print("Invalid count")
#         else:
#             indexes = []
#             if command[2] == "even":
#                 for index in range(-1, -count - 1, -1):
#                     if -len(even) > index:
#                         break
#                     indexes.insert(0, even[index])
#             elif command[2] == "odd":
#                 for index in range(-1, -count - 1, -1):
#                     if -len(odd) > index:
#                         break
#                     indexes.insert(0, odd[index])
#             print(indexes)
#     command = input().split()
#
# print(integers)