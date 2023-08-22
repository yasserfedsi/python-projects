# Program 2: Convert Celsius to Fahrenheit

def celesiusToFahrenheit(celesius):
    return  (celesius * 9 / 5) + 32

def celesiusToKelvin(celesius):
    return (celesius + 273.15)


while True:
    print("========Welcome to convertor========")
    print("Choose one of the options: ")
    print("1. Convert Celesius to Fahrenheit.")
    print("2. Convert Celsius to Kelvin.")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You chose option 1!")
        celsius = float(input("Enter celesius degree: "))  
        fahrenheit = celesiusToFahrenheit(celsius)
        print(f"{celsius} Celesius is equal to {fahrenheit} Fahrenheit.\n")
    elif choice == "2":
        print("You chose option 2!")
        celsius = float(input("Enter celesius degree: "))
        kelvin = celesiusToKelvin(celsius)
        print(f"{celsius} Celsius is equal to {kelvin} Kelvin.\n")
    elif choice == "3":
        print("Exiting the program. GoodBye!")
        break
    else:
        print("Invalid choice. Please choose a valid option")