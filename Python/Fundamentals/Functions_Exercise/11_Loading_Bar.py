def loading_bar(number):
    percent = f"{number}%"
    bar_list = ["%" if i < number/10 else "." for i in range(10)]
    bar = "".join(bar_list)
    return percent, bar


number = int(input())
percent, bar = loading_bar(number)
print(percent, end=" ")
if number == 100:
    print("Complete!")
    print(f"[{bar}]")
else:
    print(f"[{bar}]")
    print("Still loading...")
