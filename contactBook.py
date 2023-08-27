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