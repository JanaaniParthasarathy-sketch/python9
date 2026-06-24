import json

FILENAME = "students.json"

# Load data
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_data(students):
    with open(FILENAME, "w") as file:
        json.dump(students, file, indent=4)

# Grade calculation
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

students = load_data()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics")
    print("7. Save Data")
    print("8. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        students.append({
            "name": name,
            "roll": roll,
            "marks": marks,
            "grade": get_grade(marks)
        })

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No Records Found")
        else:
            for s in students:
                print("\n----------------------")
                print("Name :", s["name"])
                print("Roll :", s["roll"])
                print("Marks:", s["marks"])
                print("Grade:", s["grade"])

    # Search
    elif choice == "3":

        roll = input("Enter Roll Number: ")

        found = False

        for s in students:
            if s["roll"] == roll:
                print(s)
                found = True
                break

        if not found:
            print("Student Not Found")

    # Update
    elif choice == "4":

        roll = input("Enter Roll Number: ")

        for s in students:

            if s["roll"] == roll:

                s["name"] = input("New Name: ")
                s["marks"] = float(input("New Marks: "))
                s["grade"] = get_grade(s["marks"])

                print("Record Updated")
                break

    # Delete
    elif choice == "5":

        roll = input("Enter Roll Number: ")

        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Record Deleted")
                break

    # Statistics
    elif choice == "6":

        if len(students) == 0:
            print("No Data Available")

        else:

            total = sum(student["marks"] for student in students)

            average = total / len(students)

            highest = max(student["marks"] for student in students)

            lowest = min(student["marks"] for student in students)

            print("\n===== REPORT =====")
            print("Total Students:", len(students))
            print("Average Marks :", round(average, 2))
            print("Highest Marks :", highest)
            print("Lowest Marks  :", lowest)

    # Save
    elif choice == "7":

        save_data(students)
        print("Data Saved Successfully!")

    # Exit
    elif choice == "8":

        save_data(students)
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
