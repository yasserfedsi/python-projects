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
        print("Contact added successfully.")

    def display_contact(self):
        print("======Contacts======")
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone_number}")
            print(f"Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("-- Contact Found --")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
               self.contacts.remove(contact)
               return
        print("Contact not found.")

def main():
    contact_book = ContactBook
    
    while True:
        print("======Conatct Book======")
        print("1. Add contact")
        print("2. Display contacts")
        print("3. Search contact.")
        print("4. Delete contact.")
        print("5. Exit")