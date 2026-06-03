import csv
import os

FILE_NAME = "students.csv"

# CSV file lekapothe create cheyyi
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Grade", "Marks"])
        print(f"📁 '{FILE_NAME}' file created.\n")

# Andaru students load cheyyi
def load_students():
    students = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

# Students save cheyyi
def save_students(students):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Age", "Grade", "Marks"])
        writer.writeheader()
        writer.writerows(students)

# Student add cheyyi
def add_student():
    print("\n➕ Add New Student")
    print("-" * 30)
    students = load_students()

    # Auto ID generate cheyyi
    new_id = str(len(students) + 1)

    name  = input("Enter Name  : ").strip()
    age   = input("Enter Age   : ").strip()
    grade = input("Enter Grade : ").strip()
    marks = input("Enter Marks : ").strip()

    # Basic validation
    if not name or not age or not grade or not marks:
        print("❌ All fields are required!")
        return

    student = {"ID": new_id, "Name": name, "Age": age, "Grade": grade, "Marks": marks}
    students.append(student)
    save_students(students)
    print(f"✅ Student '{name}' added successfully with ID: {new_id}")

# Andaru students view cheyyi
def view_students():
    print("\n📋 All Students")
    print("-" * 60)
    students = load_students()

    if not students:
        print("⚠️  No students found!")
        return

    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<8} {'Marks':<6}")
    print("-" * 60)
    for s in students:
        print(f"{s['ID']:<5} {s['Name']:<20} {s['Age']:<5} {s['Grade']:<8} {s['Marks']:<6}")
    print("-" * 60)
    print(f"Total Students: {len(students)}")

# Student search cheyyi
def search_student():
    print("\n🔍 Search Student")
    print("-" * 30)
    name = input("Enter student name to search: ").strip().lower()
    students = load_students()

    found = [s for s in students if s['Name'].lower() == name]
    if found:
        print(f"\n✅ Found {len(found)} record(s):")
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<8} {'Marks':<6}")
        print("-" * 50)
        for s in found:
            print(f"{s['ID']:<5} {s['Name']:<20} {s['Age']:<5} {s['Grade']:<8} {s['Marks']:<6}")
    else:
        print(f"❌ No student found with name '{name}'")

# Student update cheyyi
def update_student():
    print("\n✏️  Update Student")
    print("-" * 30)
    students = load_students()

    if not students:
        print("⚠️  No students found!")
        return

    view_students()
    student_id = input("\nEnter Student ID to update: ").strip()

    found = False
    for s in students:
        if s['ID'] == student_id:
            found = True
            print(f"\nUpdating: {s['Name']}")
            print("(Press Enter to keep current value)\n")

            new_name  = input(f"New Name  [{s['Name']}] : ").strip()
            new_age   = input(f"New Age   [{s['Age']}]  : ").strip()
            new_grade = input(f"New Grade [{s['Grade']}]: ").strip()
            new_marks = input(f"New Marks [{s['Marks']}]: ").strip()

            if new_name:  s['Name']  = new_name
            if new_age:   s['Age']   = new_age
            if new_grade: s['Grade'] = new_grade
            if new_marks: s['Marks'] = new_marks

            save_students(students)
            print(f"✅ Student ID {student_id} updated successfully!")
            break

    if not found:
        print(f"❌ No student found with ID '{student_id}'")

# Student delete cheyyi
def delete_student():
    print("\n🗑️  Delete Student")
    print("-" * 30)
    students = load_students()

    if not students:
        print("⚠️  No students found!")
        return

    view_students()
    student_id = input("\nEnter Student ID to delete: ").strip()

    new_list = [s for s in students if s['ID'] != student_id]

    if len(new_list) == len(students):
        print(f"❌ No student found with ID '{student_id}'")
    else:
        save_students(new_list)
        print(f"✅ Student ID {student_id} deleted successfully!")

# Main menu
def main():
    initialize_file()

    while True:
        print("\n" + "=" * 40)
        print("   🎓 Student Management System")
        print("=" * 40)
        print("  1. ➕ Add Student")
        print("  2. 📋 View All Students")
        print("  3. 🔍 Search Student")
        print("  4. ✏️  Update Student")
        print("  5. 🗑️  Delete Student")
        print("  6. 🚪 Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("\n👋 Goodbye! See you soon!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
