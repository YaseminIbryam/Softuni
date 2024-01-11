number_of_pages = int(input())
pages_for_hour = int(input())
days = int(input())
hours_a_day = (number_of_pages // pages_for_hour) // days
print(hours_a_day)
