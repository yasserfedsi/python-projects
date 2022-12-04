num_1 = int (input("enter first no: "))
num_2 = int (input("enter second no: "))
num_3 = int (input("enter third no: "))

add = num_1 + num_2 + num_3
print("Addition is: ", add)

average = add / 10

if (average < 10):
    print ("You didn't succed")
    print("Your average is: ", average)
elif (average > 10):
    print("You succed with average of ", average)