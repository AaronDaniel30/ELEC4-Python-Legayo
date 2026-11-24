# Name: Aaron Daniel A. Legayo
# Section: BSIT IV-C
# Activity: P3 - Student Record Manager
# Date: November 21, 2026

students = []
student_names = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name.lower() in student_names:
        print("Student already exists!")
    else:
        students.append(name)
        student_names.add(name.lower())
        print(f"{name} successfully added!")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(student.lower())
            print(f"{student} successfully removed!")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name or part of a name: ").strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    matches = [name for name in students if keyword in name.lower()]

    if matches:
        print("\nSearch Results:")
        for name in matches:
            print(f"- {name}")
    else:
        print("No matching student found.")


def display_students():
    if not students:
        print("\nNo students recorded.")
        return

    print("\n===== STUDENT LIST =====")

    for number, name in enumerate(sorted(students, key=str.lower), start=1):
        print(f"{number}. {name}")

    print(f"\nTotal Students: {len(students)}")


def main():
    print("===================================")
    print("     STUDENT RECORD MANAGER")
    print("Student: Aaron Daniel A. Legayo")
    print("Section: BSIT IV-C")
    print("===================================")

    while True:
        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()


# LIST AND SET:
# A list stores student names and keeps their order.
# A set stores lowercase names to prevent duplicate entries.
# Lists allow duplicate values, while sets only keep unique values.
# I use the list to display and manage names, and the set to check duplicates.