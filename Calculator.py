print("Hello!! I am a calculator Use me ")
print("Press 1 to add up two numbers :\nPress 2 to get the difference of two numbers :\nPress 3 to get the product of the two number :\nPress 4 to divide two numbers :\nPress 5 to get the remainder of two numbers :\n")
choice = int(input("Please enter your choice :"))
if choice == 1:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    sum = a+b
    print("The sum of two numbers is :",sum)
elif choice == 2:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    diff = a-b
    print("The difference of two numbers is :",diff)
elif choice == 3:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    product = a*b
    print("The product of two numbers is :",product)
elif choice == 4:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    div = a/b
    print("The div of two numbers is :",div)
elif choice == 5:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    rem = a%b
    print("The remainder of two numbers is :",rem)
else:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    print("The two numbers are :",a,b)
    print("Thank You!!")
