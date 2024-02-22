def add_book(book_name, shelf):
    if book_name not in shelf:
        shelf.insert(0, book_name)
    return shelf


def take_book(book_name, shelf):
    if book_name in shelf:
        shelf.remove(book_name)
    return shelf


def swap_books(book1, book2, shelf):
    if book1 in shelf and book2 in shelf:
        index_book1 = shelf.index(book1)
        index_book2 = shelf.index(book2)
        shelf[index_book1], shelf[index_book2] = shelf[index_book2], shelf[index_book1]
    return shelf


def insert_book(book_name, shelf):
    if book_name not in shelf:
        shelf.append(book_name)
    return shelf


def check_book(index, shelf):
    if not (len(shelf) <= index or index < 0):
        print(shelf[index])


books = input().split("&")
while True:
    command = input()
    if command == "Done":
        print(", ".join(books))
        break
    command_list = command.split(" | ")
    command = command_list[0]
    if command == "Add Book":
        books = add_book(command_list[1], books)
    elif command == "Take Book":
        books = take_book(command_list[1], books)
    elif command == "Swap Books":
        books = swap_books(command_list[1], command_list[2], books)
    elif command == "Insert Book":
        books = insert_book(command_list[1], books)
    elif command == "Check Book":
        check_book(int(command_list[1]), books)