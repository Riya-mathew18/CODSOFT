print("Simple Calculator")
while True:
    print("\n--- New Calculation ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if(operation == "+"):
        print("Result:", num1 + num2)
    elif(operation == "-"):
        print("Result:", num1 - num2)
    elif(operation == "*"):
        print("Result:", num1 * num2)
    elif(operation == "/"):
        if(num2 != 0):
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operation")
    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() == "no":
        print("Thank you for using the calculator ")
        break
