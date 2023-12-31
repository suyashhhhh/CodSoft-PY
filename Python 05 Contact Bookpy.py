#Task05
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def add_contact(contact_list):
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")

    contact = Contact(name, phone_number, email, address)
    contact_list.append(contact)
    print("Contact added successfully!")

def view_contact_list(contact_list):
    if not contact_list:
        print("Contact list is empty.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contact_list, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")

def search_contact(contact_list):
    query = input("Enter name or phone number to search: ")
    results = []

    for contact in contact_list:
        if query.lower() in contact.name.lower() or query in contact.phone_number:
            results.append(contact)

    if not results:
        print("No matching contacts found.")
    else:
        print("\nSearch Results:")
        for index, result in enumerate(results, start=1):
            print(f"{index}. Name: {result.name}, Phone: {result.phone_number}")

def update_contact(contact_list):
    view_contact_list(contact_list)
    if not contact_list:
        return

    try:
        index = int(input("\nEnter the contact number to update: "))
        if 1 <= index <= len(contact_list):
            contact = contact_list[index - 1]
            contact.name = input("Enter the updated name: ")
            contact.phone_number = input("Enter the updated phone number: ")
            contact.email = input("Enter the updated email: ")
            contact.address = input("Enter the updated address: ")
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contact_list):
    view_contact_list(contact_list)
    if not contact_list:
        return

    try:
        index = int(input("\nEnter the contact number to delete: "))
        if 1 <= index <= len(contact_list):
            deleted_contact = contact_list.pop(index - 1)
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    contact_list = []

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_contact(contact_list)
            elif choice == 2:
                view_contact_list(contact_list)
            elif choice == 3:
                search_contact(contact_list)
            elif choice == 4:
                update_contact(contact_list)
            elif choice == 5:
                delete_contact(contact_list)
            elif choice == 6:
                print("Exiting the Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
