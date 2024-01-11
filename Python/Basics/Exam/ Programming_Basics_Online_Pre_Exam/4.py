number_computer_models = int(input())
number_sales = 0
sales = 0
sum_rating = 0
for model in range(number_computer_models):
    number = int(input())
    rating = number % 10
    possible_sales = number // 10
    if rating == 2:
        sales = possible_sales * 0
    elif rating == 3:
        sales = possible_sales * 0.5
    elif rating == 4:
        sales = possible_sales * 0.7
    elif rating == 5:
        sales = possible_sales * 0.85
    elif rating == 6:
        sales = possible_sales * 1
    number_sales += sales
    sum_rating += rating
average_rating = sum_rating / number_computer_models
print(f"{number_sales:.2f}")
print(f"{average_rating:.2f}")
