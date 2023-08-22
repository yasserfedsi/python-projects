# Initializing the program
def addition(P, Q):
    return P + Q

def subtraction(P, Q):
    return P - Q

def multiplication(P, Q):
    return P * Q

def division(P, Q):
    return P / Q

print("===============Welcome to PyCalculator===============")

while True:
    print("Here are the options: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Please choose one of the options: ")

    if choice == "1":
        print("You chose addition!")
        number1 = float(input("Give me the first number: "))  # Convert to float for handling decimals
        number2 = float(input("Give me the second number: ")) # Convert to float for handling decimals
        print("Result:", addition(number1, number2))
    elif choice == "2":
        print("You chose subtraction!")
        number1 = float(input("Give me the first number: "))
        number2 = float(input("Give me the second number: "))
        print("Result:", subtraction(number1, number2))
    elif choice == "3":
        print("You chose multiplication!")
        number1 = float(input("Give me the first number: "))
        number2 = float(input("Give me the second number: "))
        print("Result:", multiplication(number1, number2))
    elif choice == "4":
        print("You chose division!")
        number1 = float(input("Give me the first number: "))
        number2 = float(input("Give me the second number: "))
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", division(number1, number2))
    elif choice == "5":
        print("Exiting the program")
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")
