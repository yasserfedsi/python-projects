class User:
    def __init__(self):
        self.usersList = []

    def validPassword(self, password):
        return len(password) >= 5

    def validEmail(self, email):
        return email.lower().endswith("@gmail.com") or email.lower().endswith("@brainerx.com")

    def addUser(self, email, password):
        if not self.validPassword(password):
            print("Password must contain at least 5 characters.")
            return

        if not self.validEmail(email):
            print("Invalid email format. The email must end with '@gmail.com' or '@brainerx.com'.")
            return

        user = {"Email": email, "Password": password}
        self.usersList.append(user)
        print(f"User with email '{email}' added successfully!")

    def searchUser(self, email):
        for user in self.usersList:
            if user["Email"] == email:
                return user
        return None

    def deleteUser(self, email):
        for user in self.usersList:
            if user["Email"] == email:
                self.usersList.remove(user)
                print(f"User with email '{email}' deleted successfully!")
                return
        print(f"User with email '{email}' not found!")

    def modifyUser(self, email, new_email, new_password):
        for user in self.usersList:
            if user["Email"] == email:
                if not self.validPassword(new_password):
                    print("New password must contain at least 5 characters.")
                    return

                if not self.validEmail(new_email):
                    print("Invalid new email format. The email must end with '@gmail.com' or '@brainerx.com'.")
                    return

                user["Email"] = new_email
                user["Password"] = new_password
                print(f"User with email '{email}' modified successfully!")
                return
        print(f"User with email '{email}' not found!")

    def displayUsers(self):
        print("List of users:")
        for user in self.usersList:
            print(f"Email: {user['Email']}, Password: {user['Password']}")

def main():
    userManager = User()

    while True:
        print("==============Welcome to FindX==============")
        print("\nOptions:")
        print("1. Add a user")
        print("2. Search a user")
        print("3. Delete a user")
        print("4. Modify a user")
        print("5. Display list of users")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            userManager.addUser(email, password)
        elif choice == "2":
            email = input("Enter user email to search: ")
            user = userManager.searchUser(email)
            if user:
                print(f"User found: Email: {user['Email']}, Password: {user['Password']}")
            else:
                print(f"User with email '{email}' not found!")
        elif choice == "3":
            email = input("Enter user email to delete: ")
            userManager.deleteUser(email)
        elif choice == "4":
            email = input("Enter user email to modify: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            userManager.modifyUser(email, new_email, new_password)
        elif choice == "5":
            userManager.displayUsers()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
