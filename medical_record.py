from patient import patients_dict
from doctor import doctor_dict


medical_records_dict = {}


class MedicalRecord:

    def __init__(
        self,
        record_id,
        patient_id,
        doctor_id,
        diagnosis,
        symptoms,
        treatment,
        prescription,
        admission_date,
        discharge_date,
        status
    ):


        # VALIDATION
        if record_id <= 0:
            raise ValueError(
                "Medical Record ID must be greater than 0"
            )

        if patient_id not in patients_dict:
            raise ValueError(
                "Patient does not exist"
            )

        if doctor_id not in doctor_dict:
            raise ValueError(
                "Doctor does not exist"
            )

        if diagnosis.strip() == "":
            raise ValueError(
                "Diagnosis cannot be empty"
            )

        if symptoms.strip() == "":
            raise ValueError(
                "Symptoms cannot be empty"
            )

        if treatment.strip() == "":
            raise ValueError(
                "Treatment cannot be empty"
            )

        if prescription.strip() == "":
            raise ValueError(
                "Prescription cannot be empty"
            )

        if admission_date.strip() == "":
            raise ValueError(
                "Admission date cannot be empty"
            )

        # Discharge date can initially be empty
        # because patient may still be admitted.

        if status not in ["Admitted", "Discharged"]:
            raise ValueError(
                "Status must be Admitted or Discharged"
            )

        if status == "Discharged" and discharge_date.strip() == "":
            raise ValueError(
                "Discharge date is required for discharged patient"
            )

        
        # STORE DATA
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.symptoms = symptoms
        self.treatment = treatment
        self.prescription = prescription
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.status = status


    # DISPLAY ONE RECORD
    def display_record(self):

        print("-" * 45)

        print("Medical Record ID:", self.record_id)
        print("Patient ID:", self.patient_id)
        print("Doctor ID:", self.doctor_id)
        print("Diagnosis:", self.diagnosis)
        print("Symptoms:", self.symptoms)
        print("Treatment:", self.treatment)
        print("Prescription:", self.prescription)
        print("Admission Date:", self.admission_date)
        print("Discharge Date:", self.discharge_date)
        print("Status:", self.status)

        print("-" * 45)


# SAVE MEDICAL RECORDS
def save_medical_records():

    with open("medical_record.txt", "w") as f:

        for record in medical_records_dict.values():

            f.write(
                f"{record.record_id},"
                f"{record.patient_id},"
                f"{record.doctor_id},"
                f"{record.diagnosis},"
                f"{record.symptoms},"
                f"{record.treatment},"
                f"{record.prescription},"
                f"{record.admission_date},"
                f"{record.discharge_date},"
                f"{record.status}\n"
            )


# LOAD MEDICAL RECORDS

def load_medical_records():

    try:

        with open("medical_record.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split(",")

                record_id = int(data[0])
                patient_id = int(data[1])
                doctor_id = int(data[2])
                diagnosis = data[3]
                symptoms = data[4]
                treatment = data[5]
                prescription = data[6]
                admission_date = data[7]
                discharge_date = data[8]
                status = data[9]

                record = MedicalRecord(
                    record_id,
                    patient_id,
                    doctor_id,
                    diagnosis,
                    symptoms,
                    treatment,
                    prescription,
                    admission_date,
                    discharge_date,
                    status
                )

                medical_records_dict[record_id] = record

    except FileNotFoundError:

        print(
            "No medical record file found. "
            "Starting with empty medical records."
        )



# ADD MEDICAL RECORD
def add_medical_record():

    try:

        record_id = int(
            input("Enter Medical Record ID: ")
        )

        if record_id in medical_records_dict:

            raise ValueError(
                "Medical Record ID already exists"
            )

        patient_id = int(
            input("Enter Patient ID: ")
        )

        doctor_id = int(
            input("Enter Doctor ID: ")
        )

        diagnosis = input(
            "Enter Diagnosis: "
        )

        symptoms = input(
            "Enter Symptoms: "
        )

        treatment = input(
            "Enter Treatment: "
        )

        prescription = input(
            "Enter Prescription: "
        )

        admission_date = input(
            "Enter Admission Date: "
        )

        discharge_date = input(
            "Enter Discharge Date "
            "(leave empty if still admitted): "
        )

        # Decide status automatically

        if discharge_date.strip() == "":
            status = "Admitted"
        else:
            status = "Discharged"

        # Create object

        record = MedicalRecord(
            record_id,
            patient_id,
            doctor_id,
            diagnosis,
            symptoms,
            treatment,
            prescription,
            admission_date,
            discharge_date,
            status
        )

        # Store object

        medical_records_dict[record_id] = record

        # Save file

        save_medical_records()

        print(
            "\nMedical record successfully added!"
        )

    except ValueError as e:

        print(
            "Error:",
            e
        )



# VIEW ALL MEDICAL RECORDS
def view_medical_records():

    if not medical_records_dict:

        print(
            "No medical records found."
        )

        return

    print(
        "\n========== ALL MEDICAL RECORDS =========="
    )

    for record in medical_records_dict.values():

        record.display_record()



# SEARCH MEDICAL RECORD
def search_medical_record():

    try:

        if not medical_records_dict:

            print(
                "No medical records found."
            )

            return

        record_id = int(
            input(
                "Enter Medical Record ID "
                "you want to search: "
            )
        )

        if record_id in medical_records_dict:

            record = medical_records_dict[
                record_id
            ]

            print(
                "\nMedical Record Found!"
            )

            record.display_record()

        else:

            print(
                "Medical Record Not Found."
            )

    except ValueError:

        print(
            "Medical Record ID must be a number."
        )


# UPDATE MEDICAL RECORD

def update_medical_record():

    try:

        if not medical_records_dict:

            print(
                "No medical records found."
            )

            return

        record_id = int(
            input(
                "Enter Medical Record ID "
                "you want to update: "
            )
        )

        if record_id not in medical_records_dict:

            print(
                "Medical Record Not Found."
            )

            return

        record = medical_records_dict[
            record_id
        ]

        print(
            "\nCurrent Medical Record:"
        )

        record.display_record()

        # New information

        new_diagnosis = input(
            "Enter new Diagnosis: "
        )

        new_symptoms = input(
            "Enter new Symptoms: "
        )

        new_treatment = input(
            "Enter new Treatment: "
        )

        new_prescription = input(
            "Enter new Prescription: "
        )

        # Validation

        if new_diagnosis.strip() == "":
            raise ValueError(
                "Diagnosis cannot be empty"
            )

        if new_symptoms.strip() == "":
            raise ValueError(
                "Symptoms cannot be empty"
            )

        if new_treatment.strip() == "":
            raise ValueError(
                "Treatment cannot be empty"
            )

        if new_prescription.strip() == "":
            raise ValueError(
                "Prescription cannot be empty"
            )

        # Update object

        record.diagnosis = new_diagnosis
        record.symptoms = new_symptoms
        record.treatment = new_treatment
        record.prescription = new_prescription

        save_medical_records()

        print(
            "\nMedical Record successfully updated."
        )

    except ValueError as e:

        print(
            "Error:",
            e
        )


# DISCHARGE PATIENT
def discharge_patient():

    try:

        if not medical_records_dict:

            print(
                "No medical records found."
            )

            return

        record_id = int(
            input(
                "Enter Medical Record ID "
                "you want to discharge: "
            )
        )

        if record_id not in medical_records_dict:

            print(
                "Medical Record Not Found."
            )

            return

        record = medical_records_dict[
            record_id
        ]

        # Already discharged

        if record.status == "Discharged":

            print(
                "Patient is already discharged."
            )

            return

        print(
            "\nPatient Medical Record:"
        )

        record.display_record()

        discharge_date = input(
            "Enter Discharge Date: "
        )

        if discharge_date.strip() == "":

            raise ValueError(
                "Discharge date cannot be empty"
            )

        confirm = input(
            "Are you sure to discharge "
            "(yes/no): "
        )

        if confirm.lower() == "yes":

            record.discharge_date = discharge_date
            record.status = "Discharged"

            save_medical_records()

            print(
                "\nPatient successfully discharged."
            )

        else:

            print(
                "\nDischarge cancelled."
            )

    except ValueError as e:

        print(
            "Error:",
            e
        )


# DELETE MEDICAL RECORD
def delete_medical_record():

    try:

        if not medical_records_dict:

            print(
                "No medical records found."
            )

            return

        record_id = int(
            input(
                "Enter Medical Record ID "
                "you want to delete: "
            )
        )

        if record_id not in medical_records_dict:

            print(
                "Medical Record Not Found."
            )

            return

        record = medical_records_dict[
            record_id
        ]

        print(
            "\nMedical Record to be deleted:"
        )

        record.display_record()

        confirm = input(
            "Are you sure to delete "
            "(yes/no): "
        )

        if confirm.lower() == "yes":

            del medical_records_dict[
                record_id
            ]

            save_medical_records()

            print(
                "Medical Record successfully deleted."
            )

        else:

            print(
                "Deletion cancelled."
            )

    except ValueError:

        print(
            "Medical Record ID must be a number."
        )




def medical_record_menu():
    # MEDICAL RECORD MENU

    # LOAD OLD MEDICAL RECORDS
    load_medical_records()  
    while True:
        print("\n" + "*" * 45)

        print(
            "Welcome to Medical Record Management Module"
        )

        print("*" * 45)

        print("1. Add Medical Record")
        print("2. View All Medical Records")
        print("3. Search Medical Record")
        print("4. Update Medical Record")
        print("5. Discharge Patient")
        print("6. Delete Medical Record")
        print("7. Back to Main Menu")

        print("*" * 45)

        choice = input(
            "Enter your choice: "
        )

        # ADD

        if choice == "1":

            add_medical_record()

        # VIEW

        elif choice == "2":

            view_medical_records()

        # SEARCH

        elif choice == "3":

            search_medical_record()

        # UPDATE

        elif choice == "4":

            update_medical_record()

        # DISCHARGE

        elif choice == "5":

            discharge_patient()

        # DELETE

        elif choice == "6":

            delete_medical_record()

        # BACK

        elif choice == "7":

            print(
                "\nReturning to Main Menu..."
            )

            break

        else:

            print(
                "Invalid choice! "
                "Please select 1-7."
            )