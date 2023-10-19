# user input
book = input()
input_line = input()

# logic
count = 0
book_found = False
while input_line != "No More Books":
    if input_line == book:
        book_found = True
        break
    count += 1
    input_line = input()

# code output
if book_found:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")
