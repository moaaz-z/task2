class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def show_doctors(self):
        for doctor in self.doctors:
            print("Name:", doctor.name)
            print("Specialty:", doctor.specialty)

    def show_patients(self):
        for patient in self.patients:
            print("Name:", patient.name)
            print("Illness:", patient.illness)


class Doctor(Hospital):
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []

    def assign_patient(self, patient):
        self.patients.append(patient)

    def show_patients(self):
        for patient in self.patients:
            print(patient.name)


class Patient(Hospital):
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Illness:", self.illness)

        if self.doctor:
            print("Doctor:", self.doctor.name)
        else:
            print("Doctor: No doctor assigned")

while True:
    print("\n========== Hospital Management System ==========")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Show Doctors")
    print("4. Show Patients")
    print("5. Assign Patient to Doctor")
    print("6. Assign Doctor to Patient")
    print("7. Show Doctor's Patients")
    print("8. Show Patient Information")
    print("9. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter Doctor Name: ")
        specialty = input("Enter Doctor Specialty: ")
        doctor = Doctor(name, specialty)
        Hospital.add_doctor(doctor)
        print("Doctor added successfully.")

    elif choice == 2:
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        illness = input("Enter Patient Illness: ")
        patient = Patient(name, age, illness)
        Hospital.add_patient(patient)
        print("Patient added successfully.")

    elif choice == 3:
        Hospital.show_doctors()

    elif choice == 4:
        Hospital.show_patients()

    elif choice == 5:
        # Assign a patient to a doctor
        patient_name=input('Enter Patient Name: ')
        doctor_name=input('Enter Doctor Name: ')
        for patient in Hospital.patients:
           if patient_name==Patient.name:
               for doctor in Hospital.doctors:
                   if doctor_name==Doctor.name:
                       Doctor.assign_patient(patient_name)
                       print("Patient assigned to doctor successfully.")
                       break
                   break
               

    elif choice == 6:
        # Assign a doctor to a patient
        patient_name = input("Enter Patient Name: ")
        doctor_name = input("Enter Doctor Name: ")

        for patient in Hospital.patients:
            if patient.name == patient_name:
                for doctor in Hospital.doctors:
                    if doctor.name == doctor_name:
                        patient.assign_doctor(doctor)
                        print("Doctor assigned to patient successfully.")
                        break
                break

    elif choice == 7:
        # Show a doctor's patients
        doctor_name = input("Enter Doctor Name: ")

        for doctor in Hospital.doctors:
            if doctor.name == doctor_name:
                doctor.show_patients()
                break

    elif choice == 8:
        # Show patient information
        patient_name = input("Enter Patient Name: ")

        for patient in Hospital.patients:
            if patient.name == patient_name:
                patient.show_info()
                break

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")