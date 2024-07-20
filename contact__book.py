def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print(f'Contact "{name}" added.')


def view_contacts(contacts):
    if contacts:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")


def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if
                      search_term in contact['name'] or search_term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print(
                f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")


def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print(f'Contact "{contact["name"]}" updated.')
            return
    print("No contacts found to update.")


def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.remove(contact)
            print(f'Contact "{contact["name"]}" deleted.')
            return
    print("No contacts found to delete.")


def main():
    contacts = []

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
