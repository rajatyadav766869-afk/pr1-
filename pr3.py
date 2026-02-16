allstudent = []

def add_student(studentid, student_name, age, grade, dob, subject):
    student = {
        "studentID": studentid,
        "student_Name": student_name,
        "Age": age,
        "Grade": grade,
        "DOB": dob,
        "Subject": subject,
    }
    allstudent.append(student)
    return f"Student added successfully! ID={studentid}, Name={student_name}, Age={age}, Grade={grade}, DOB={dob}, Subject={subject}"

def display_students():
    if not allstudent:
        print("\nNo students to display.\n")
        return
    
    print("\n display All Students:")
    for student in allstudent:
        print(f"ID: {student['studentID']}, Name: {student['student_Name']}, Age: {student['Age']}, Grade: {student['Grade']}, DOB: {student['DOB']}, Subject: {student['Subject']}")

def update_student():
    student_id = int(input("Enter the Student ID to update: "))
    for student in allstudent:
        if student["studentID"] == student_id:
            print("Leave blank to keep current value.")
            new_name = input(f"New name (current: {student['student_Name']}): ") or student["student_Name"]
            new_age = input(f"New age (current: {student['Age']}): ")
            new_grade = input(f"New grade (current: {student['Grade']}): ") or student["Grade"]
            new_dob = input(f"New DOB (current: {student['DOB']}): ") or student["DOB"]
            new_subject = input(f"New subject (current: {student['Subject']}): ") or student["Subject"]

            student["student_Name"] = new_name
            student["Age"] = int(new_age) if new_age else student["Age"]
            student["Grade"] = new_grade
            student["DOB"] = new_dob
            student["Subject"] = new_subject

            print("Student updated successfully.\n")
            return
    print("Student ID not found.\n")

def delete_student():
    student_id = int(input("\nEnter the Student ID to delete: "))
    for student in allstudent:
        confirm = input("Are you sure you want to delete this student?(yes/no): ").lower()
        if confirm == "yes":
            if student["studentID"] == student_id:
              allstudent.remove(student)
              print("Student deleted successfully.\n")
              return
        else:
            print("cancel deletion ")
    print("Student ID not found.\n")

# MAIN MENU
while True:
    print("\nWelcome to the Student Data Organizer!")
    print("Select an option: ")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Exit")

    try:
        option = int(input("Select an option: "))
        match option:
            case 1:
                studentID = int(input("Enter student ID: "))
                studentname = input("Enter student name: ")
                age = int(input("Enter age: "))
                grade = input("Enter grade: ")
                dob = input("Enter DOB (DD-MM-YYYY): ")
                subject = input("Enter subject: ")
                result = add_student(studentID, studentname, age, grade, dob, subject)
                print(result)
            case 2:
                display_students()
            case 3:
                update_student()
            case 4:
                delete_student()
            case 5:
                print("Thank you for using the Student Data Organizer!")
                break
            case _:
                print("Invalid option. Please select between 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")