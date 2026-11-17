
import json

books = []


# LOAD DATA
def load_data():
    global books
    with open("books.json", "r") as file:
        books = json.load(file)

def load_students():
     global students
     with open("student.json", "r") as file:
      students = json.load(file)
def save_Student():
    with open("student.json", "w") as file:
              json.dump(students, file, indent=4)


# SAVE DATA
def save_data():
    with open("books.json", "w") as file:
         json.dump(books, file, indent=4)




def load_issue_books():
    global issued_books
    with open("issued_books.json", "r") as file:
        issued_books = json.load(file)

def save_issued_books():
     with open("issued_books.json", "w") as file:
      json.dump(issued_books, file, indent=4)


# ADD BOOKS
def add_books():
    load_data()

    Book_id = input("Enter Book ID: ")

    for book in books:
        if book["Book ID"] == Book_id:
            print("Error: This Book ID already exists!")
            return

    Book_name = input("Enter Book Name: ")
    Book_author = input("Enter Book Author Name: ")
    Book_quantity = int(input("Enter Book Quantity: "))

    if Book_quantity <= 0:
        print("Invalid quantity!")
        return

    my_dict = {
        "Book ID": Book_id,
        "Book name": Book_name,
        "Author": Book_author,
        "quantity": Book_quantity
    }

    books.append(my_dict)
    save_data()

    print("Book Added Successfully!")


# DISPLAY BOOKS
def display_books():
    load_data()

    print("\n")
    print("=" * 70)
    print("              LIBRARY BOOK RECORDS")
    print("=" * 70)

    print(f"{'Book ID':<12} | {'Book Name':<18} | {'Author':<18} | {'Quantity':<10}")

    print("-" * 75)

    for book in books:
        print(f"{book['Book ID']:<12} | {book['Book name']:<18} | {book['Author']:<18} | {book['quantity']:<10}")

    if not books:
        print("No books available.")


# SEARCH BOOKS
def search_books():

    load_data()

    print("============ SEARCH BOOKS =================")
    print("1. Search by Book ID")
    print("2. Search by Book Name")
    print("3. Search by Author Name")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")

        for book in books:
            if book["Book ID"] == book_id:
                print("Book Name:", book["Book name"])
                print("Author:", book["Author"])
                break
        else:
            print("Book not found")

    elif choice == "2":
        book_name = input("Enter Book Name: ")

        for book in books:
            if book["Book name"].lower() == book_name.lower():
                print("Book Name:", book["Book name"])
                print("Author:", book["Author"])
                break
        else:
            print("Book not found")

    elif choice == "3":
        author_name = input("Enter Author Name: ")

        for book in books:
            if book["Author"].lower() == author_name.lower():
                print("Book Name:", book["Book name"])
                print("Author:", book["Author"])
                break
        else:
            print("Book not found")

    else:
        print("Invalid choice")



def register_students():
    load_students()


def register_students():
    load_students()

    Student_id = input("Enter Student ID: ")

    for student in students:
        if student["Student ID"] == Student_id:
            print("Invalid Registration! Student ID already exists.")
            return

    Student_name = input("Enter Student Name: ")
    Student_department = input("Enter Department: ")
    Student_contactno = input("Enter Contact Number: ")

    my_dict = {
        "Student ID": Student_id,
        "Student name": Student_name,
        "Department": Student_department,
        "Contact No.": Student_contactno
    }

    students.append(my_dict)
    save_Student()

    print("Student Registered Successfully!")
def issue_books():

        load_data()
        load_students()
        load_issue_books()

        Student_id = input("Enter Student ID: ")
        student_found = False

        for student in students:
            if student["Student ID"] == Student_id:
                student_found = True
                break

        if not student_found:
            print("Error: Student is not registered!")
            return

        Book_id = input("Enter Book ID: ")
        book_found = False

        for book in books:
            if book["Book ID"] == Book_id:
                book_found = True
                break

        if not book_found:
            print("Error: Book does not exist!")
            return

        if book["quantity"] <= 0:
            print("Error: Book is not available!")
            return

        Issue_date = input("Enter Issue Date (DD-MM-YYYY): ")

        book["quantity"] -= 1

        issue_record = {
            "Student ID": Student_id,
            "Book ID": Book_id,
            "Issue Date": Issue_date
        }

        issued_books.append(issue_record)

        save_data()
        save_issued_books()

        print("Book Issued Successfully!")
def return_book():

        load_data()
        load_issue_books()

        Student_id = input("Enter Student ID: ")
        Book_id = input("Enter Book ID: ")

        issue_found = False

        for record in issued_books:
            if record["Student ID"] == Student_id and record["Book ID"] == Book_id:
                issue_found = True
                break

        if not issue_found:
            print("Error: No issue record found!")
            return

        for book in books:
            if book["Book ID"] == Book_id:
                book["quantity"] += 1
                break

        issued_books.remove(record)

        save_data()
        save_issued_books()

        print("Book Returned Successfully!")


def delete_book():
    load_issue_books()
    load_data()
    book_id = input("Enter Book ID to delete: ")
    book_found = False
    print("books")

    for book in books:
        if book["Book ID"] == book_id:
            book_found = True
            break

    if not book_found:
        print("Error: Book does not exist!")
        return
    for issue in issued_books:
        if issue["Book ID"] == book_id:
            print("This Book is currently issue")
            return
    books.remove(book)
    save_data()
    print("Book deleted successfully!")










while True:
    print("=================================")
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("=================================")

    print("2. Add Books")
    print("3. Display Books")
    print("4. Search Books")
    print("5. Register Student")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Display Issue Book")
    print("9. Delete Books")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
      add_books()

    elif choice == "3":
     display_books()

    elif choice == "4":
     search_books()

    elif choice == "5":
     register_students()

    elif choice == "6":
     issue_books()

    elif choice == "7":
     return_book()

    elif choice == "9":
     delete_book()

    elif choice == "10":
     print("Exiting Library Management System.")
     break
    else:
     print("Invalid choice! Please try again.")
