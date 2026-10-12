
books = {
    "Python_Basics": "John",
    "AI_Fundamentals": "David"
}

for i in range(3):
    title = input("Enter book title: ")
    if title in books:
        print("Author:", books[title])
    else:
        print("Book not found")
