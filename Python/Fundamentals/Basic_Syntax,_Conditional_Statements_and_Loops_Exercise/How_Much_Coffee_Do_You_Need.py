event = input()
coffees = 0
while event != "END":
    if event.islower():
        coffee = 1
    else:
        coffee = 2
    event = event.lower()
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffees += coffee
    event = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
