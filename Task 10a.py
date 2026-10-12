
students = {"Ravi": "CSE", "Priya": "ECE"}

for i in range(3):
    name = input("Enter student name: ")
    if name in students:
        print("Department:", students[name])
    else:
        print("Student not found")
