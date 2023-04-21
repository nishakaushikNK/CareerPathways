import math 

print("Welcome to world of calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Square Root")
print("8. Power")
print("0. Exit")
op = int(input("Please select an operation ex: 1 : "))


def completeOperation(operation):
    if operation == 1:
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print(firstNum, " plus ", secondNum, " is ", (firstNum + secondNum))
    elif operation == 2:
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print(firstNum, " minus ", secondNum, " is ", (firstNum - secondNum))
    elif operation == 3:
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print(firstNum, " times ", secondNum, " is ", (firstNum * secondNum))
    elif operation == 4:
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print(firstNum, " divided by ", secondNum, " is ", (firstNum / secondNum))
    elif operation == 5:
        num = int(input("Please enter the number you'd like to square: "))
        print(num, " squared is ", (num**2))
    elif operation == 6:
        num = int(input("Please enter the number you'd like to cube: "))
        print(num, "squared is ", (num**3))
    elif operation == 7:
        num = int(input("Please enter the number you'd like to square root: "))
        print("The square root of ", num, " is ", (math.sqrt(num)))
    elif operation == 8:
        firstNum = int(input("Please enter your base: "))
        secondNum = int(input("Please enter your exponent: "))
        print(firstNum, " to the power of ", secondNum, " is ", (firstNum ** secondNum))
    elif operation == 0:
        print("Bye!")


while op != 0:
    completeOperation(op)
    op = int(input("Please select an operation ex: 1 : "))
