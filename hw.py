# Part 1 : Initializing the system

# Valide password
def validPassword(password):
    return len(password) >= 5


# Valid email
def validEmail(email):
    return email.lower().endWith('@gmail.com') or email.lower().endsWith('@brainerx.com')

# Add user
def addUser(userList, email, password):
    if not validPassword(password):
        print("Password must contain at least 5 charachters")
        return

    if not validEmail(email):
        print("Invalid email format. Email must end with '@gmail.com' or '@brainerx.com' ")
        return
    
    user = {
        "Email": email,
        "Password": password
    }

    userList.append(user)
    print("User added successfully.")

# Search user
def searchUser(userList, email):
    for user in userList:
        if user["Email"] == email:
            return user
    return None

# Delete user
def deleteUser(userList, email):
    for user in userList:
        if user["Email"] == email:
            userList.remove(user)
            print("User deleted successfully.")
            return
    print("User not found")

# Modify user
def modifyUser(userList, email, newEmail, newPassword):
    for user in userList:
        if user["Email"] == email:
            user["Email"] = newEmail
            user["Password"] = newPassword
            print(f"User with email '{email}' modified successfully.")
            return
    print(f"User with email '{email}' not found. ")

# Display Users
def displayUsers(userList):
    print("List of users:")
    for user in userList:
        print(f"Email: {user['Email']}, Password: {user['Password']}")

# Main screen
def main():
    userList = []
    while True:
        print("============Welcome to FindX============")
        print("\nChoose one of this functions: ")
        print("1. Add a user.")
        print("2. Search for a user.")
        print("3. Delete a user.")
        print("4. Modify a user.")
        print("5. Display list of users.")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            addUser(userList, email, password)
        elif choice == "2":
            email = input("Enter user email to search for: ")
            user = searchUser(userList, email)
            if user == True:
                 print(f"User found: Email: {user['Email']}, Password: {user['Password']}")
            else:
                print("User not found!")
        elif choice == "3":
            email = input("Enter user email to delete")
            deleteUser(userList, email)
        elif choice == "4":
            email = input("Enter user email to modify: ")
            newEmail = input("Enter new email: ")
            newPassword = input("Enter new password: ")
            modifyUser(userList, email, newEmail, newPassword)
        elif choice == "5":
            displayUsers(userList)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try a correct function.")


        
    
if __name__ == "__main__":
    main()