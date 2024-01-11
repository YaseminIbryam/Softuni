target_book = input()
command = input()
books_count = 0
book_found = False
while command != "No More Books":
    current_book = command
    if current_book == target_book:
        book_found = True
        break
    books_count += 1
    command = input()

if book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
