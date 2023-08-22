# Program: Calculate the Average of Numbers

# Initializing the program
def calculateAverage():
    # Step 1: Ask the user for the total number of elements
    total_elements = int(input("Enter the total number of elements: "))

    # Step 2: Create an empty list to store the numbers
    numbers = []

    # Step 3: Ask the user to enter each number and store them in the list
    for element in range(total_elements):
        num = float(input(f"Enter element {element + 1}: "))
        numbers.append(num)
    # Step 4: Calculate the sum of all numbers in the list
    total_sum = sum(numbers)
    
    # Step 5: Calculate the average
    average = total_sum / total_elements

    # Step 6: Display the average to the user
    print(f"The average of numbers is: {average}")

# Call the function to run the program
calculateAverage()