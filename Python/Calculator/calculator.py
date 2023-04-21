import math as m
print("Welcome to world of calculator")
print("JTCaclculator\n1:Add\n2:subtract\n3:multiply\n4:Divide\n5:Root\n6:Power")

a=int(input("First Number"))
op = input("Which operation?")
b=int(input("Second Number"))

if op=="3":
    result=int(a)*int(b)
    print(result)
elif op=="1":
    result=a+b
    print(result)
elif op=="2":
    result=a-b
    print(result)
elif op=="4":
    result=a/b
    print(result)
elif op=="5":
    result=m.pow(a,(1/b))
    print(result)
elif op=="6":
    result=m.pow(a,b)
    print(result)