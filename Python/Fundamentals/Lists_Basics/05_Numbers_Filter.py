# lines = int(input())
# numbers = []
# filtered_numbers = []
# for line in range(lines):
#     num = int(input())
#     numbers.append(num)
# command = input()
# for num in numbers:
#     match command:
#         case "even":
#             if num % 2 == 0:
#                 filtered_numbers.append(num)
#         case "odd":
#             if num % 2 != 0:
#                 filtered_numbers.append(num)
#         case "negative":
#             if num < 0:
#                 filtered_numbers.append(num)
#         case "positive":
#             if not num < 0:
#                 filtered_numbers.append(num)
# print(filtered_numbers)

# lines = int(input())
# numbers = []
# filtered_numbers = []
#
# for line in range(lines):
#     num = int(input())
#     numbers.append(num)
#
# command = input()
#
# for num in numbers:
#     if command == "even" and num % 2 == 0:
#         filtered_numbers.append(num)
#     elif command == "odd" and num % 2 != 0:
#         filtered_numbers.append(num)
#     elif command == "negative" and num < 0:
#         filtered_numbers.append(num)
#     elif command == "positive" and not num < 0:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)

n = int(input())
numbers = [int(input()) for line in range(n)]
command = input()
filtered_numbers = []
for number in numbers:
    filtered_command = ("even" and number % 2 == 0 or
                        command == "odd" and number % 2 != 0 or
                        command == "negative" and number < 0 or
                        command == "positive" and number >= 0)
    if filtered_command:
        filtered_numbers.append(number)
print(filtered_numbers)
