students = {}

def showMenu():
    print("1. Add Student")
    print("2. Update Students")
    print("3. Delete Student")
    print("4. View all")
    print("5. Search students")
    print("6. Show total number of students")
    print("7. Exit")

def addStudent(db):
    roll_no = input("Enter roll no ")
    if roll_no in db:
        print("Already Exists")
        return
    name = input("Enter name ")
    db[roll_no] = name
    print("student added")

def updateStudent(db):
    roll_no = input("Enter roll no to update ")
    if roll_no  in db:
        name = input("Enter new name ")
        db[roll_no] = name
        print("student updated")
    else:
        print("Student not found")

def deleteStudent(db):
    roll_no = input("Enter roll no to delete")
    if roll_no in db:
        del db[roll_no]
        print("student deleted")
    else:
        print("Student not found")

def viewAll(db):
    if db:
        print("All Students : ")
        for roll_no,name in db.items():
            print(f"Roll No: {roll_no}, Name: {name}")
    else:
        print("No students found")

def searchStudents(db):
    roll_no = input("Enter roll no to search")
    if roll_no in db:
        print(f"Roll No: {roll_no}, Name: {db[roll_no]}")
    else:
        print("Student not found")

def totalStudents(db):
    print(f"Total number of students: {len(db)}")

while True:
    showMenu()
    choice = input("Enter your choice: ")

    if choice == '1':
        addStudent(students)
    elif choice == '2':
        updateStudent(students)
    elif choice == '3':
        deleteStudent(students)
    elif choice == '4':
        viewAll(students)
    elif choice == '5':
        searchStudents(students)
    elif choice == '6':
        totalStudents(students)
    elif choice == '7':
        print("Exiting the proggram")
        break
    else:
        print("Invalid choice")