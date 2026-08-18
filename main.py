from patient import patient_menu
from doctor import doctor_menu
from appointement import appointement_menu
from medical_record import medical_record_menu


def main_menu():

    while True:

        print("\n" + "=" * 45)
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Medical Record Management")
        print("5. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            patient_menu()

        elif choice == "2":

            doctor_menu()

        elif choice == "3":

            appointement_menu()

        elif choice == "4":

            medical_record_menu()

        elif choice == "5":

            print("\nThank you for using Hospital Management System.")
            print("Program ended.")
            break

        else:

            print(
                "Invalid choice! "
                "Please select 1-5."
            )


if __name__ == "__main__":
    main_menu()