def palindromeChecker():
    palindrome = input("Enter a word/phrase/number: ")
    palindromeLwr = palindrome.lower()
    palindromeNoSpaces = palindrome.replace(" ", "")

    if palindromeNoSpaces == palindromeNoSpaces[::-1]:
        print(f"{palindrome} is a palindrome.")
    else:
        print(f"{palindrome} is not a palindrome.")

while True:
    print("==============Welcome to Palindrome Checker==============")
    print("Commands: ")
    print("Start checking.")
    print("Exit")

    choice = input("Enter you command: ")

    if choice == "1":
        palindromeChecker()
    elif choice == "2":
        print("Goodbye!")
        break
