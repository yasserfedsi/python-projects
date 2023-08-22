def maxNumber():
    # Step 1: Ask the user to input three numbers, one by one
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    # Step 2: Compare the three numbers to find the maximum value
    maximum_number = max(number1, number2, number3)

    # Step 3: Display the maximum number to the user
    print(f"Maximum number in the list is: {maximum_number}")

maxNumber()