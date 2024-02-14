notes = [" "] * 10
command = input().split("-")
while command[0] != "End":
    importance = int(command[0])
    index = importance - 1
    note = command[1]
    notes.pop(index)
    notes.insert(index, note)
    command = input().split("-")
notes = [note for note in notes if not note == " "]
print(notes)
