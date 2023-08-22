def calculateFactorial():
    while True:
        print("==========Welcome to FactorialCalculator==========")
        print("Here are the options: ")
        print("1. Start calculating")
        print("2. Exit")

        choice = input("Enter the option you want: ")

        if choice == "1":
            # Step 1: Ask the user to input a positive integer
            n = int(input("Enter a positive integer: "))

            # Step 2: Initialize the factorial variable to 1
            factorial = 1

            # Step 3: Calculate the factorial using a loop
            for i in range(1, n + 1):
                factorial *= i

            # Step 4: Display the factorial to the user
            print(f"The factorial of {n} is: {factorial}")
        elif choice == "2":
            print("Take care. Goodbye")
            break
        else:
            print("Invalid option. Please enter a valid option!")

# Call the function to run the program
calculateFactorial()
