import math

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def square(num):
    return num*num

def cube(num):
    return num**3

def squareRoot(num):
    return math.sqrt(num)

def power(base, power):
    return base**power

print("Welcome to world of calculator")
print("Please select an operation: ")
print("1. Add")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")
print("5. Square")
print("6. Cube ")
print("7. Square root ")
print("8. Power ")
print("0. Exit ")
answer = float(input("Please select an operation: "))

while answer!=0:
    if answer==1 or answer==2 or answer==3 or answer==4:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        if (answer==1):
            print(num1, " plus ", num2, " equals ", add(num1,num2))
        elif (answer==2):
            print(num1, " minus ", num2, " equals ", subtract(num1,num2))
        elif (answer==3):
            print(num1, " times ", num2, " equals ", multiply(num1,num2))
        else:
            print(num1, " divided by ", num2, " equals ", divide(num1,num2))
    elif answer==5 or answer==6 or answer==7:
        perform = float(input("Enter your number: "))
        if (answer==5):
            print(perform, " squared is ", square(perform))
        elif (answer==6):
            print(perform, " cubed is ", cube(perform))
        else:
            print("The square root of ", perform, " is ", squareRoot(perform))
    elif answer==8:
        base = float(input("What is your base: "))
        pow = float(input("Enter your power: "))
        print(base, " to the power of ", pow, " is ", power(base,pow))
    answer = float(input("Please select an operation: "))

print("Ok, thanks for playing!")
