doctor_dict = {}

class Doctor:

    def __init__(self,doctor_id,name,age,specilaization):
        if doctor_id <= 0:
            raise ValueError("doctor id must be grater than 0")
        if name.strip() == "":
            raise ValueError("doctor name must not me empty")
        if age <=0:
            raise ValueError("doctor age must be grater than 0")
        if specilaization.strip() == "":
            raise ValueError("doctor name must not me empty")

        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.specilaization = specilaization

    def display_doctor(self):
        for doctor in doctor_dict.values():
            print("-" *30)
            print("Doctor ID: ",doctor.doctor_id)
            print("Doctor name: ",doctor.name)
            print("Doctor age: ",doctor.age)
            print("Doctor speciaization: ",doctor.specilaization)
            print("-" *30)

    def search_doctor(self):
        if not doctor_dict:
            print("No doctors found.")
            return
        doctor_id = int(input("Enter the doctor_id you want to search: "))
        if doctor_id in doctor_dict:
            doctor = doctor_dict[doctor_id]
            print("Doctor found...")
            print("-" *30)
            print("Doctor ID: ",doctor.doctor_id)
            print("Doctor name: ",doctor.name)
            print("Doctor age: ",doctor.age)
            print("Doctor speciaization: ",doctor.specilaization)
            print("-" *30)
        else:
            print("Doctor Not found...")

    def update_doctor_info(self):
        doctor_id = int(input("Enter the doctor_id you want to update information: "))
        if doctor_id <= 0:
            raise ValueError("doctor id must be grater than 0")
        if doctor_id in doctor_dict:
            new_name = input("Enter the name of doctor: ")
            new_doctor_age = int(input("Enter doctor Age: "))
            new_doctor_specialization = input("Enter specializtion of doctor: ")
            if new_name.strip() == "":
                raise ValueError("doctor name must not me empty")
            if  new_doctor_age<=0:
                raise ValueError("doctor age must be grater than 0")
            if new_doctor_specialization.strip() == "":
                raise ValueError("doctor name must not me empty")
            self.name = new_name
            self.age = new_doctor_age
            self.specilaization= new_doctor_specialization
            save_doctor()
            print("Successfully updated Doctor Information")

        else:
            print("Doctor not Found...")
        
    def delete_doctor(self):
        if not doctor_dict:
            print("No doctors found.")
            return
        doctor_id = int(input("Enter the doctor_id you want to Delete: "))

        if doctor_id not in doctor_dict:
            print("Doctor ID Not Found...")

        else:

            doctor = doctor_dict[doctor_id]
            print("Deleted Doctor Information...")
            print("-" *30)
            print("Doctor ID: ",doctor.doctor_id)
            print("Doctor name: ",doctor.name)
            print("Doctor age: ",doctor.age)
            print("Doctor speciaization: ",doctor.specilaization)
            print("-" *30)

            confirm = input("Are you sure to delete (yes/no): ")
            if confirm.lower() == 'yes':
                del doctor_dict[doctor_id]
                save_doctor()
                print("Successflly Deleted")
            else:
                print("\nDeletion cancelled.")

def save_doctor():
    try:
        with open("Doctor.txt","w") as f:
            for doctor in doctor_dict.values():
                f.write(f"{doctor.doctor_id},{doctor.name},{doctor.age},{doctor.specilaization}\n")
    except FileNotFoundError:
        print("File Not Found")

def load_doctor():
    try:
        with open("Doctor.txt","r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                data = line.split(",")
                doctor_id = int(data[0])
                dotor_name = data[1]
                doctor_age = int(data[2])
                doctor_specialization = data[3]
                doctor = Doctor(doctor_id,dotor_name,doctor_age,doctor_specialization)
                doctor_dict[doctor_id] = doctor
    except FileNotFoundError:
        print("File not found!")



def doctor_menu():
    load_doctor()
    try:
        while True:
            print("-" * 35)
            print("Welcome to Doctor  Management Module")
            print("*" * 35)
            print("1.add doctor")
            print("2.view all doctors")
            print("3.search doctor")
            print("4.update doctor")
            print("5.delete doctor")
            print("Back to main menue")
            print("*" * 35)

            ch = input("\nEnter yor choice: ")
            if ch == '1':
                doctor_id = int(input("Enter the doctor id: "))
                if doctor_id in doctor_dict:
                    raise ValueError("doctor id already exist")
                name = input("Enter the name of doctor: ")
                doctor_age = int(input("Enter doctor Age: "))
                doctor_specialization = input("Enter specializtion of doctor: ")
                doctor = Doctor(doctor_id,name,doctor_age,doctor_specialization)
                doctor_dict[doctor_id] = doctor
                save_doctor()
                print("Successfullu added doctor")

            elif ch == '2':
                doctor.display_doctor()

            elif ch == '3':
                doctor.search_doctor()

            elif ch =='4':
                doctor.update_doctor_info()

            elif ch == '5':
                        doctor.delete_doctor()
            elif ch =='6':
                print("\nReturning to Main Menu...")
                break
            else:
                print("Invalid choice! Please select 1-6...")

    except ValueError as e:
        print("Error! ",e)