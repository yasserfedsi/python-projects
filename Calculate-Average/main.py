num_1 = int (input("enter no: "))
num_2 = int (input("enter no: "))
num_3 = int (input("enter no: "))
num_4 = int (input("enter no: "))
num_5 = int (input("enter no: "))
num_6 = int (input("enter no: "))
num_7 = int (input("enter no: "))
num_8 = int (input("enter no: "))
num_9 = int (input("enter no: "))
num_10 = int (input("enter no: "))

add = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10
print("Addition is: ", add)

average = add / 10

if (average < 10):
    print ("You didn't succed")
    print("Your average is: ", average)
elif (average > 10):
    print("You succed with average of ", average)