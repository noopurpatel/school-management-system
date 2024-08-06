# KATHY SIERRA
# TP123456

# Part 1: Display Menu
def displayMenu():
    print("*" * 32)
    print("=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. Update Student")
    print("3. List all students")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Exit")
    print("*" * 32)

# Part 2: Add, View and Validate Student’s Record

def addStudent():
    print("=== ADD NEW STUDENT ===")
    studentID = input("Enter Student ID: ")
    while not studentID.isdigit():
        studentID = input("Invalid Input! Please enter a valid Student ID: ")
    studentName = input("Enter Student Name: ")
    while not studentName.isalpha():
        studentName = input(
            "Invalid Input! Please enter a valid Student Name: ")
    studentAge = input("Enter Student Age: ")
    while not studentAge.isdigit():
        studentAge = input("Invalid Input! Please enter a valid Student Age: ")
    studentEmail = input("Enter Student Email: ")
    while not "@" in studentEmail:
        studentEmail = input(
            "Invalid Input! Please enter a valid Student Email: ")
    studentRecord = {"ID": studentID, "Name": studentName,
                     "Age": studentAge, "Email": studentEmail}
    studentList.append(studentRecord)
    print("New Student Added Successfully!\n")

def viewAllStudents():
    print("=== VIEW ALL STUDENTS ===")
    if len(studentList) == 0:
        print("No Student Records Found!")
    else:
        for student in studentList:
            print("ID: ", student["ID"])
            print("Name: ", student["Name"])
            print("Age: ", student["Age"])
            print("Email: ", student["Email"])
            print("=" * 32)

# Part 3: List and Search Record

def searchStudent():
    print("=== SEARCH STUDENT ===")
    studentID = input("Enter Student ID: ")
    while not studentID.isdigit():
        studentID = input("Invalid Input! Please enter a valid Student ID: ")
    for student in studentList:
        if studentID == student["ID"]:
            print("ID: ", student["ID"])
            print("Name: ", student["Name"])
            print("Age: ", student["Age"])
            print("Email: ", student["Email"])
            print("=" * 32)
            return
    print("No Student Record Found with ID: ", studentID)

def deleteStudent():
    print("=== DELETE STUDENT ===")
    studentID = input("Enter Student ID: ")
    while not studentID.isdigit():
        studentID = input("Invalid Input! Please enter a valid Student ID: ")
    for student in studentList:
        if studentID == student["ID"]:
            studentList.remove(student)
            print("Student Record Deleted Successfully!")
        return

    print("No Student Record Found with ID: ", studentID)

def updateStudent():
    print("=== UPDATE STUDENT ===")
    studentID = input("Enter Student ID: ")
    while not studentID.isdigit():
        studentID = input("Invalid Input! Please enter a valid Student ID: ")
    for student in studentList:
        if studentID == student["ID"]:
            studentName = input("Enter Updated Student Name: ")
            while not studentName.isalpha():
                studentName = input(
                    "Invalid Input! Please enter a valid Student Name: ")
            studentAge = input("Enter Updated Student Age: ")
            while not studentAge.isdigit():
                studentAge = input(
                    "Invalid Input! Please enter a valid Student Age: ")
            studentEmail = input("Enter Updated Student Email: ")
            while not "@" in studentEmail:
                studentEmail = input(
                    "Invalid Input! Please enter a valid Student Email: ")
            student["Name"] = studentName
            student["Age"] = studentAge
            student["Email"] = studentEmail
            print("Student Record Updated Successfully!")
            return
    print("No Student Record Found with ID: ", studentID)

studentList = []

while True:
    displayMenu()
    choice = input("Enter Your Choice: ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 6:
        choice = input("Invalid Input! Please enter a valid choice: ")
    if choice == "1":
        addStudent()
    elif choice == "2":
        updateStudent()
    elif choice == "3":
        viewAllStudents()
    elif choice == "4":
        searchStudent()
    elif choice == "5":
        deleteStudent()
    elif choice == "6":
        # exit the program
        print("Thank you for using the Student Management System!")
        exit()
