# 1. List operations
books = ["Python Basics", "Data Structures", "Algorithms", "Web Development"]

# Adding and removing books
books.append("Machine Learning")
books.remove("Web Development")

# Sorting and reversing
books.sort()
print("Sorted Books:", books)

books.reverse()
print("Reversed Books:", books)

# Indexing and slicing
print("First book (Indexing):", books[0])
print("First two books (Slicing):", books[:2])

# 2. Dictionary for librarian details
librarian = {
    "name": "Sarah Connor",
    "id": "LIB882",
    "shift": "Morning"
}

# Modifying and adding key-value pairs
librarian["shift"] = "Evening"
librarian["department"] = "Main Library"
print("\nLibrarian Details:", librarian)

# 3. Converting two lists into a dictionary using dict() and zip()
book_ids = [101, 102, 103, 104]
book_titles = ["Python Basics", "Data Structures", "Algorithms", "Machine Learning"]

book_directory = dict(zip(book_ids, book_titles))
print("\nBook Directory:", book_directory)