class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        print("--- Contacts ---")
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("--- Contact Found ---")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("======= Contact Book =======")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)

        elif choice == "2":
            contact_book.display_contacts()

        elif choice == "3":
            search_name = input("Enter name to search: ")
            contact_book.search_contact(search_name)

        elif choice == "4":
            delete_name = input("Enter name to delete: ")
            contact_book.delete_contact(delete_name)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
