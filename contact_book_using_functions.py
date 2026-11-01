print("***** CONTACT BOOK MANAGEMENT SYSTEM *****")

contacts = {
    "yeshu": 8764689790,
    "sai": 9100055758,
    "kumar": 630986535,
    "nithish": 6306547652,
    "karthik": 9823465077
}


def add_contact():
    name = input("Enter name: ").strip()
    number = input("Enter phone number: ").strip()

    if not number.isdigit() or len(number) != 10:
        print("Please enter a valid 10-digit phone number.")
        return

    contacts[name] = number
    print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    number = input("Enter new phone number: ").strip()
    if not number.isdigit() or len(number) != 10:
        print("Please enter a valid 10-digit phone number.")
        return

    contacts[name] = number
    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nSaved Contacts:")
    for name, number in contacts.items():
        print(name, ":", number)


def main():
    while True:
        print("\n1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View contacts")
        print("6. Exit")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue

        if option == 1:
            add_contact()
        elif option == 2:
            search_contact()
        elif option == 3:
            update_contact()
        elif option == 4:
            delete_contact()
        elif option == 5:
            view_contacts()
        elif option == 6:
            print("Thank you for using Contact Book.")
            break
        else:
            print("Enter a valid option.")


if __name__ == "__main__":
    main()
