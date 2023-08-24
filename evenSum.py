def calculateEvenSum():
    # Step 1: Asking the user to enter two numbers
    starting_num = int(input("Enter the first number: "))
    ending_number = int(input("Enter the ending number: "))

    # Step 2: Calculate the sum of even numbers in the range
    i = starting_num
    even_sum = 0
    while i <= ending_number:
        if i % 2 == 0:
            even_sum += i
        i += 1

    # Step 3: Display the sum of even numbers
    print("The sum of even numbers in the range is:", even_sum)

while True:
    print("==============Welcome to evenSumCalculator==============")
    print("Commands: ")
    print("1. Start calculating")
    print("2. Exit")

    choice = input("Enter a command: ")

    if choice == "1":
        calculateEvenSum()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please enter a valid command.")