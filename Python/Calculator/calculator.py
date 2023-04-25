#math library
import math as m

numbers={1:"one",2:"two"}
def intro():
    print("Welcome to world of calculator")
    print("JTCaclculator\n1:Add\n2:subtract\n3:multiply\n4:Divide\n5:Root\n6:Power\n0:exit")

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mult(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def root(a,b):
    return(m.pow(a,(1/b)))
def pow(a,b):
    return(m.pow(a,b))

funcL=[add,sub,mult,div,root,pow]

def logic(op,num1,num2):
    return funcL[op-1](num1,num2)

def main():
    intro()
    operation=int(input("choose an operation: "))
    if operation==0:
        print("Left JT Claculaotr")
    else:
        num1=int(input("FirstNumber: "))
        num2=int(input("Second Number: "))
        print(logic(operation,num1,num2))

main()