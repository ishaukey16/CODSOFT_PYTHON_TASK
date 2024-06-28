print("-------SIMPLE CALCULATOR-------")
while True:
    NUM1 = int(input("Enter first number here: "))
    NUM2 = int(input("Enter second number here: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = int(input("Enter your choice from 1-5:  "))

    if choice == 1:
        Addition = NUM1 + NUM2
        print("Result:", Addition)

    elif choice == 2:
        Subtract = NUM1 - NUM2
        print("Result:", Subtract)

    elif choice == 3:
        Multiply = NUM1 * NUM2
        print("Result:", Multiply)

    elif choice == 4:
        if NUM2 != 0:
            Divide = NUM1 / NUM2
            print("Result:", Divide)
        else:
            print("Error: division by zero is not allowed")

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid Input")




