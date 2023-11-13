def binary_to_decimal(binary_number):
    # Initialize variables
    size = len(binary_number)
    decimal_result = 0

    # Iterate through each bit of the binary number
    for i in range(size):
        # Convert the binary character to an integer
        bit = int(binary_number[size - 1 - i])
        
        # Add the bit to the resulting value by multiplying with the corresponding power of 2
        decimal_result += bit * (2**i)

    # Display the result
    print(f"The binary number {binary_number} is equivalent to {decimal_result} in decimal.")

while True:
    print("========Welcome to BinDec Calculator========")
    print("Select an option: ")
    print("1. Start calculating.")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You chosed option 1")
        ask = input("Enter your binary number: ")
        binary_to_decimal(ask)
    elif choice == "2":
        print("Good bye!")
        break