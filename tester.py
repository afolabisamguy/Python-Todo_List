from testing import MyClass


def main():
    while True:
        print("\n1. Create new instance\n2. Edit instances\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            MyClass.create_instance()
        elif choice == '2':
            MyClass.edit_instances()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
