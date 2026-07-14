def display_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def start_program():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 6:
            print("Thank you for using Student Management System!")
            break

        elif 1 <= choice <= 5:
            print("Feature coming soon...")

        else:
            print("Invalid choice! Please try again.")


start_program()

