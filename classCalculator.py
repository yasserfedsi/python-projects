class Calculating:
    def __init__(self, P: float, Q: float):
        self.P = P
        self.Q = Q

    def addition(self):
        return self.P + self.Q

    def subtraction(self):
        return self.P - self.Q

    def multiplication(self):
        return self.P * self.Q

    def division(self):
        try:
            return self.P / self.Q
        except ZeroDivisionError:
            print("Can't divide by 0. Please enter a valid number.")

while True:
    print("Welcome to pyCalculator")
    print("Please choose one of the following options: ")
    print("1. addition")
    print("2. subtraction")
    print("3. multiply")
    print("4. division")
    print("5. Exit")

    choice = input("Enter a valid option: ")

    if choice == "5":
        print("Have a nice day! Goodbye.")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    calc = Calculating(num1, num2)

    if choice == "1":
        print("You selected addition. Result is:", calc.addition())
    elif choice == "2":
        print("You selected subtraction. Result is:", calc.subtraction())
    elif choice == "3":
        print("You selected multiplication. Result is:", calc.multiplication())
    elif choice == "4":
        result = calc.division()
        if result is not None:
            print("You selected division. Result is:", result)
    else:
        print("Invalid option. Please choose a valid option.")
