
patients = {}
def main():
    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. View Patient Report")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Search Patient")
        print("7. Hospital Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patients()
        elif choice == "2":
            view_all_patients()
        elif choice == "3":
            view_patient_result()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            search_patient()
        elif choice == "7":
            hospital_statistics()
        elif choice == "8":
            print("Exiting program...")
        else:
            print("Invalid choice! Please select the correct choice.")

def add_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        print("Patient ID already exists!")
        return
    
    name = input("Enter Full Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    diagnosis = input("Enter Diagnosis: ")

    treatments = {}

    print("Enter at least 2 treatments: ")
    for i in range(2):
        treatment_name = input(f"Treatment {i+1} name: ")

        while True: 
            try:
                cost = float(input(f"Cost for {treatment_name}: "))
                if cost > 0:
                    break
                else: 
                    print("Cost must be positive!")
            except:
                print("Invalid input! Enter a number.")
        
        treatments[treatment_name] = cost

    patients[patient_id] = {
        "name" : name,
        "age" : age,
        "gender" : gender,
        "diagnosis" : diagnosis,
        "treatments" : treatments
    }

    print("Patient added successfully!")

def view_all_patients():
    if not patients:
        print("No patients found.")
        return
    
    print("\n--- ALL PATIENTS ---")
    for pid, details in patients.items():
        print(f"ID: {pid}, Name: {details['name']}, Diagnosis: {details['diagnosis']}")

def view_patient_report():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return
    
    patient = patients[pid]

    print("\n--- PATIENT REPORT---")
    print(f"ID: {pid}")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Gender: {patient['gender']}")
    print(f"Diagnosis: {patient['diagnosis']}")

    total = 0
    print("\nTreatments: ")
    for treatment, cost in patient["treatments"].items():
        print(f"{treatment}: {cost}")
        total += cost
    
    print(f"\nTOTAL BILL: {total}")

def update_patient():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return
    
    patient = patients[pid]

    print("\n1. Update Diagnosis")
    print("2. Add Treatment")
    print("3. Update Treatment Cost")
    print("4. Remove Treatment")

    choice = input("Choose option: ")

    if choice == "1":
        patient["diagnosis"] = input("Enter new diagnosis: ")
        print("Diagnosis updated.")

    elif choice == "2":
        t_name = input("Enter cost: ")

        while True:
            try:
                cost = float(input)("Enter cost: ")
                if cost > 0:
                    break
                else: 
                    print("Cost must be positive!")
            except:
                print("Invalid input!")

            patient["treatments"][t_name] = cost
            print("Treatment added.")
    elif choice == "3":
        t_name = input("Enter treatment name to update: ")
        if t_name in patient["treatments"]:
            while True:
                try:
                    cost = float(input("Enter new cost: "))
                    if cost > 0:
                        break
                    else:
                        print("Cost must be positive!")
                except:
                    print("Invalid input!")

            patient["treatments"][t_name] = cost
            print("Cost updated.")
        else:
            print("Treatment not found!")

    elif choice == "4":
        t_name = input("Enter treatment name to remove: ")
        if t_name in patient["treatments"]:
            del patient["treatments"][t_name]
            print("Treatment removed.")
        else:
            print("Treatment not found!")

    else:
        print("Invalid option!")

def delete_patient():
    pid =input("Enter Patirnt ID: ")

    if pid in patients:
        del patients[pid]
        print("Patient deleted successfully.")
    else:
        print("Patient not found!")

def search_patient():
    search = input("Enter Patient ID or Name: ").lower()

    found = False

    for pid, details in patients.items():
        if search == pid.lower() or search in details["name"].lower():
            print(f"ID: {pid}, Name: {details['name']}, Diagnosis: {details['diagnosis']}")
            found = True

        if not found:
            print("No matching patient found.")

def hospital_statistics():
    if not patients:
        print("No data available.")
        return
    
    total_patients = len(patients)
    total_revenue = 0

    highest = ("", 0)
    lowest = ("", float(int))

    for pid, details in patients.items():
        bill = sum(details["treatments"].values())
        total_revenue += bill

        if bill > highest[1]:
            highest = (details["name"], bill)

        if bill < lowest[1]:
            lowest = (details["name"], bill)


        print("\n--- HOSPITAL STATISTICS ---")
        print(f"Total Patients: {total_patients}")
        print(f"Total Revenue: {total_revenue}")
        print(f"Highest Bill: {highest[0]} ({highest[1]})")
        print(f"Lowest Bill: {lowest[0]} ({lowest[1]})")