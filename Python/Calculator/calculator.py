import math

def Addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Multiplication(num1, num2):
    return num1 * num2

def Division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2
    
def Squaring(num1):
    return num1**2

def cube(num1):
    return num1**3

def Squareroot(num1):
    return math.sqrt(num1)

def Power(num1, num2):
    return num1**num2

def begin():
    print("Welcome to the calculator!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Square root")
    print("8. Power")
    print("0. Exit")
    choice = int(input("Enter your choice:"))
    calc(choice)
    
    
def calc(choice):
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second numer:"))
        if choice == 1:
            result = Addition(num1, num2)
            displayanswer(result)
            begin()
        elif choice == 2:
            result = Subtraction(num1, num2)
            displayanswer(result)
            begin()
        elif choice == 3:
            result = Multiplication(num1, num2)
            displayanswer(result)
            begin()
        elif choice == 4:
            result = Division(num1, num2)
            if result == "Cannot divide by zero":
                print(result)
                begin()
            else:
                displayanswer(result)
                begin()
    elif choice == 5 or choice == 6 or choice == 7:
        num1 = float(input("Enter number:"))
        if choice == 5:
            result = Squaring(num1)
            displayanswer(result)
            begin()
        elif choice == 6:
            result = cube(num1)
            displayanswer(result)
            begin()
        elif choice == 7:
            result = Squareroot(num1)
            displayanswer(result)
            begin()
    elif choice == 8:
        num1 = float(input("Enter base number:"))
        num2 = float(input("Enter power:"))
        result = Power(num1, num2)
        displayanswer(result)
        begin()
    elif choice == 0:
        print("See you next time!")
    else:
        print("Not a valid selection")
        begin()

def displayanswer(answer):
    print("The answer is", answer)


begin()