from patient import patients_dict
from doctor import doctor_dict
appointments_dict = {}
class Appointment:

    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        
        # VALIDATION
        if appointment_id <= 0:
            raise ValueError(
                "Appointment ID must be greater than 0"
            )

        if patient_id not in patients_dict:
            raise ValueError(
                "Patient does not exist"
            )

        if doctor_id not in doctor_dict:
            raise ValueError(
                "Doctor does not exist"
            )

        if date.strip() == "":
            raise ValueError(
                "Appointment date cannot be empty"
            )

        if time.strip() == "":
            raise ValueError(
                "Appointment time cannot be empty"
            )


        # STORE DATA
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

        # Initial status
        self.status = "Booked"


    # DISPLAY APPOINTMENT(1 not all)
    def display_appointment(self):

        print("-" * 40)

        print(
            "Appointment ID:",
            self.appointment_id
        )

        print(
            "Patient ID:",
            self.patient_id
        )

        print(
            "Doctor ID:",
            self.doctor_id
        )

        print(
            "Date:",
            self.date
        )

        print(
            "Time:",
            self.time
        )

        print(
            "Status:",
            self.status
        )

        print("-" * 40)


# CHECK DOCTOR AVAILABILITY
def doctor_already_booked(doctor_id, date, time):

    for appointment in appointments_dict.values():

        if (
            appointment.doctor_id == doctor_id
            and appointment.date == date
            and appointment.time == time
            and appointment.status == "Booked"
        ):

            return True

    return False


# SAVE APPOINTMENTS
def save_appointments():

    with open("appointment.txt", "w") as f:

        for appointment in appointments_dict.values():

            f.write(
                f"{appointment.appointment_id},"
                f"{appointment.patient_id},"
                f"{appointment.doctor_id},"
                f"{appointment.date},"
                f"{appointment.time},"
                f"{appointment.status}\n"
            )



# LOAD APPOINTMENTS
def load_appointments():

    try:

        with open("appointment.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":
                    continue

                data = line.split(",")

                appointment_id = int(data[0])
                patient_id = int(data[1])
                doctor_id = int(data[2])
                date = data[3]
                time = data[4]
                status = data[5]

                appointment = Appointment(
                    appointment_id,
                    patient_id,
                    doctor_id,
                    date,
                    time
                )

                # Restore saved status
                appointment.status = status

                appointments_dict[appointment_id] = appointment

    except FileNotFoundError:

        print(
            "No appointment file found. "
            "Starting with empty appointments."
        )


# BOOK APPOINTMENT
def book_appointment():

    try:

        appointment_id = int(
            input("Enter Appointment ID: ")
        )

        # Check duplicate ID
        if appointment_id in appointments_dict:

            raise ValueError(
                "Appointment ID already exists"
            )


        patient_id = int(
            input("Enter Patient ID: ")
        )

        # Check patient
        if patient_id not in patients_dict:

            raise ValueError(
                "Patient does not exist"
            )


        doctor_id = int(
            input("Enter Doctor ID: ")
        )

        # Check doctor
        if doctor_id not in doctor_dict:

            raise ValueError(
                "Doctor does not exist"
            )


        date = input(
            "Enter Appointment Date: "
        )

        time = input(
            "Enter Appointment Time: "
        )


        # Check doctor availability
        if doctor_already_booked(
            doctor_id,
            date,
            time
        ):

            raise ValueError(
                "Doctor is already booked "
                "at this date and time"
            )


        # Create appointment
        appointment = Appointment(
            appointment_id,
            patient_id,
            doctor_id,
            date,
            time
        )


        # Store in dictionary
        appointments_dict[appointment_id] = appointment


        # Save to file
        save_appointments()


        print(
            "\nAppointment successfully booked!"
        )


    except ValueError as e:

        print(
            "Error:",
            e
        )


# VIEW ALL APPOINTMENTS
def view_appointments():

    if not appointments_dict:

        print(
            "No appointments found."
        )

        return


    print(
        "\n========== ALL APPOINTMENTS =========="
    )

    for appointment in appointments_dict.values():

        appointment.display_appointment()


# SEARCH APPOINTMENT
def search_appointment():

    try:

        if not appointments_dict:

            print(
                "No appointments found."
            )

            return


        appointment_id = int(
            input(
                "Enter Appointment ID "
                "you want to search: "
            )
        )


        if appointment_id in appointments_dict:

            appointment = appointments_dict[
                appointment_id
            ]

            print(
                "\nAppointment Found!"
            )

            appointment.display_appointment()


        else:

            print(
                "Appointment Not Found."
            )


    except ValueError:

        print(
            "Appointment ID must be a number."
        )

def cancel_appointment():

    try:

        if not appointments_dict:

            print(
                "No appointments found."
            )

            return


        appointment_id = int(
            input(
                "Enter Appointment ID "
                "you want  to cancel: "
            )
        )


        if appointment_id not in appointments_dict:

            print(
                "Appointment Not Found."
            )

            return


        appointment = appointments_dict[
            appointment_id
        ]


        # Already cancelled?
        if appointment.status == "Cancelled":
            print(
                "Appointment is already cancelled."
            )

            return


        print(
            "\nAppointment to be cancelled:"
        )

        appointment.display_appointment()


        confirm = input(
            "Are you sure to cancel? (yes/no): "
        )


        if confirm.lower() == "yes":

            appointment.status = "Cancelled"
            save_appointments()

            print(
                "Appointment successfully cancelled."
            )


        else:

            print(
                "Cancellation cancelled."
            )


    except ValueError:

        print(
            "Appointment ID must be a number."
        )





# APPOINTMENT MENU

def appointement_menu():
    # LOAD OLD APPOINTMENTS
    load_appointments()
    while True:
        print("\n" + "*" * 40)

        print(
            "Welcome to Appointment Management Module"
        )

        print("*" * 40)

        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Search Appointment")
        print("4. Cancel Appointment")
        print("5. Back to Main Menu")

        print("*" * 40)


        choice = input(
            "Enter your choice: "
        )


        # BOOK
        if choice == "1":

            book_appointment()


        
        # VIEW
        elif choice == "2":

            view_appointments()


        
        # SEARCH
        elif choice == "3":

            search_appointment()


        # CANCEL
        elif choice == "4":

            cancel_appointment()


        
        # BACK
        elif choice == "5":

            print(
                "\nReturning to Main Menu..."
            )

            break


        else:

            print(
                "Invalid choice! "
                "Please select 1-5."
            )