
# Name: Aaron Daniel Legayo
# Section: IV-BSIT
# Activity: P5 - Student Information File System
# Date: November 23, 2026

FILE_NAME = "set2/p5/students.txt"


# Load existing student records from the text file
def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "course": data[2],
                        "average": float(data[3])
                    }
                    students.append(student)

    except FileNotFoundError:
        print("No existing student records found. Starting with an empty list.")

    return students


# Save all student records to the text file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student['id']}|{student['name']}|"
                f"{student['course']}|{student['average']}\n"
            )


# Add a new student
def add_student(students):
    print("\n--- ADD STUDENT ---")

    student_id = input("Enter Student ID: ").strip()

    if any(student["id"] == student_id for student in students):
        print("Error: Student ID already exists.")
        return

    name = input("Enter Full Name: ").strip()
    course = input("Enter Course/Section: ").strip()

    if not student_id or not name or not course or "|" in name or "|" in course:
        print("Error: Invalid or empty information.")
        return

    try:
        average = float(input("Enter General Average: "))

        if not 0 <= average <= 100:
            print("Error: Average must be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "course": course,
            "average": average
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter a valid number for the average.")


# Display all student records
def display_students(students):
    print("\n--- ALL STUDENT RECORDS ---")

    if not students:
        print("No student records available.")
        return

    for student in students:
        print("------------------------------")
        print(f"Student ID: {student['id']}")
        print(f"Full Name: {student['name']}")
        print(f"Course/Section: {student['course']}")
        print(f"General Average: {student['average']:.2f}")

    print("------------------------------")
    print(f"Total Students: {len(students)}")


# Search for a student using their ID
def search_student(students):
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print(f"Student ID: {student['id']}")
            print(f"Full Name: {student['name']}")
            print(f"Course/Section: {student['course']}")
            print(f"General Average: {student['average']:.2f}")
            return

    print("Student not found.")


# Update existing student information
def update_student(students):
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Leave a field blank to keep its current value.")

            new_name = input("Enter New Full Name: ").strip()
            new_course = input("Enter New Course/Section: ").strip()

            if new_name:
                if "|" in new_name:
                    print("Error: Invalid character in name.")
                    return
                student["name"] = new_name

            if new_course:
                if "|" in new_course:
                    print("Error: Invalid character in course.")
                    return
                student["course"] = new_course

            try:
                new_average = input("Enter New General Average: ").strip()

                if new_average:
                    average = float(new_average)

                    if not 0 <= average <= 100:
                        print("Error: Average must be between 0 and 100.")
                        return

                    student["average"] = average

                save_students(students)
                print("Student information updated successfully!")
                return

            except ValueError:
                print("Error: Please enter a valid number.")
                return

    print("Student not found.")


# Main menu
def main():
    students = load_students()

    while True:
        print("\n================================")
        print("   STUDENT INFORMATION SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            print("Thank you for using the Student Information System!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
