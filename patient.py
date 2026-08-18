patients_dict ={}
class Patient:
    def __init__(self,id,name,age,disease):
        if id <= 0:
            raise ValueError("patient id must be greater than 0")
        if name.strip() == "":
            raise ValueError("Patient name cannot be empty")
        if age <=0:
            raise ValueError("Patient age must be greater than 0")
        if disease.strip() == "":
             raise ValueError("Patient name cannot be empty")
    
        self.id = id
        self.name = name
        self.age = age
        self.disease = disease

    def display_patient(self):
        for patient in patients_dict.values():
            print("-"* 35)
            print("patient_id: ",patient.id)
            print("patient name: ",patient.name)
            print("patient age: ",patient.age)
            print("patient disease: ",patient.disease)
            print("-"* 35)
    def search_patient(self):
        patient_id = int(input("Enter patient id: "))
        if patient_id in patients_dict:
            print("patient Found")
            print("-"* 35)
            print("patient id: ",self.id)
            print("patient name: ",self.name)
            print("patient age: ",self.age)
            print("patient disease: ",self.disease)
            print("-"* 35)

        else:
            print("patient Not Found")

    def update_patient(self):
        patient_id = int(input("Enter patient id: "))
        
        if patient_id in patients_dict:
            

                new_name = input("enter the patient name: ")
                new_age = int(input("Enter patent age: "))
                disease = input("Enter patient disease: ")
                if new_name.strip() == "":
                    raise ValueError("Patient name cannot be empty")
                if new_age <= 0:
                    raise ValueError("Patient age must be greater than 0")

                if disease.strip() == "":
                    raise ValueError("Patient disease cannot be empty")
                #update object
                self.name = new_name
                self.age = new_age
                self.disease = disease
                print("Successfully update")
        else:
             print("Patient Not Found")

    def delete_patient(self):
        try:

            patient_id = int(input("Enter patient id you want to delete: "))
            
            if patient_id not in patients_dict:
                print("patient id not found")
                return
            else:
                print("Patient to be deleted...")
                PATIENT = patients_dict[patient_id]  #it return values of patient_id that we want and store in patient 
                print("-"* 35)
                print("patient id: ",PATIENT.id)
                print("patient name: ",PATIENT.name)
                print("patient age: ",PATIENT.age)
                print("patient disease: ",PATIENT.disease)
                print("-"* 35)                                       
                confirm = input("Are you sure to delete (yes/no): ")
                if confirm.lower() == 'yes':
                    del patients_dict[patient_id]
                    print("Successfully deleted patient")
                else:
                    print("\nDeletion cancelled.")
        except ValueError:
            print("id must be a number ")


def save_patient():
    with open("patient.txt","w") as f:
        for patient in patients_dict.values():
            f.write(f" {patient.id},{patient.name},{patient.age},{patient.disease}\n")

def load_patient():
    try:

        with open("patient.txt","r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                else:
                    data = line.split(",")
                    patient_id = int(data[0])
                    patient_name = data[1]
                    patient_age =int(data[2])
                    patient_disease = data[3]

                            #again make object why: rogram dobara start hone par purana object khatam ho jata hai,
                            #  is liye file mein saved data se naya Patient object banate hain.
                            #aur itinary mai add bhi abb karay gai
                    patient = Patient(patient_id,patient_name,patient_age,patient_disease)
                    patients_dict[patient_id] = patient
    except FileNotFoundError:
        print("File not found!")



def patient_menu():
    load_patient()
    try:
        choice = 'y'
        while choice == 'y' or choice == 'Y':
            print("*" * 35)
            print("Welcome to Patient Management Module")
            print("*" * 35)
            print("1.add patient")
            print("2.view all patients")
            print("3.search patient")
            print("4.update patient")
            print("5.delete patient")
            print("Back to main menue")

            ch = input("Enter yor choice: ")
            if ch == '1':
                
                patient_id = int(input("Enter the patient id: "))
                if patient_id in patients_dict:
                    raise ValueError("patient id already exist")
                patient_name = input("Enter patient_name: ")
                patient_age = int(input("Enter Patient Age: "))
                patient_disease = (input("Enter patient Disease: "))
                patient = Patient(patient_id,patient_name,patient_age,patient_disease)
                patients_dict[patient_id] = patient
                save_patient()

            elif ch == '2':
                patient.display_patient()
            elif ch == '3':
                patient.search_patient()
            elif ch == '4':
                patient.update_patient()
            elif ch == '5':
                patient.delete_patient()
            elif ch =='6':
                print("\nReturning to Main Menu...")
                break
            else:
                print("Invalid choice! Please select 1-6...")

    except ValueError as e:
        print("Error!",e)


