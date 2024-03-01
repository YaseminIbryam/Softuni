lowercase = [element.lower() for element in input().split()]
elements_dict = {element: lowercase.count(element) for element in lowercase}
for key, value in elements_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
