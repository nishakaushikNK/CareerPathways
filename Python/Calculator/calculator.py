import math as m

def Addition(number1, number2):
    return number1+number2

def Subtract(number1, number2):
    return number1-number2

def Multiply(number1, number2):
    return number1*number2

def Divide(number1, number2):
    return number1/number2

def Percentage(number1, number2):
    return int((number1/number2) * 100)

def Power(number1, number2):
    return int((m.pow(number1, number2)))


check = 1
while check == 1:
    print("Welcome to world of calculator")
    print("Please select an operation:")
    print("")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Power")
    print("7. Exit")
    print("")
    Selection = int(input("Select the Operator: "))
    if Selection == 7: 
        check == 0
    else: 
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        print("")
        if Selection==1:
            print("The result of Addition is: ", Addition(number1, number2))
        elif Selection==2:
            print("The result of Subtraction is: ", Subtract(number1, number2))
        elif Selection==3:
            print("The result of Multiplication is: ", Multiply(number1, number2))
        elif Selection==4:
            print("The result of Division is: ", Divide(number1, number2))
        elif Selection==5:
            print("The percentage is:",Percentage(number1, number2),"%")
        elif Selection==6:
            print("The result is: ", Power(number1, number2))






