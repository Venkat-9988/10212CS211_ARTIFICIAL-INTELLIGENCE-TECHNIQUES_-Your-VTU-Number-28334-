
doctors = {
    "Dr_Ravi": "Cardiology",
    "Dr_Priya": "Neurology"
}

for i in range(3):
    specialization = input("Enter specialization: ")
    found = False

    for doctor, field in doctors.items():
        if field.lower() == specialization.lower():
            print("Doctor:", doctor)
            found = True

    if not found:
        print("No doctor found")
