print("Hello, it's my first program on python")
i = "y"
while i == "y":

    numberone = int(input("Enter first number: "))
    numertwo = int(input("Enter second number: "))
    choice = input("What the action to perform? (+, -, *, /): ")

    if choice == "+":
        print("Answer = ", numberone + numertwo)
    elif choice == "-":
        print("Answer = ", numberone - numertwo)
    elif choice == "*":
        print("Answer = ", numberone * numertwo)
    elif choice == "/":
        if numberone <= 0:
            print("Error, it is impossible to fulfill the request, it is impossible to divide by zero ")
        else:
            ("Answer = ", numberone / numertwo)

    i = input("Do you want to refresh? y/n: ")
