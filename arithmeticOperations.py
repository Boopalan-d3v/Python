print("_________Arithmetic Operations_________\n")
print("__ADDITION__")
def add(a,b):   #creating a function()
    add=a+b     #performing additional operation
    print (f"the addition value is {add}\n")    #the output statement
add(int(input("Enter a value: ")),int(input("Enter b value: ")))    #dynamically get inputs from user and pass it to the function variables

print("___SUBRACTION___")
def sub(a,b):   #creating another new funtion()
    sub=a-b
    print (f"the Subraction value is {sub}\n")
sub(int(input("Enter a value: ")),int(input("Enter b value: ")))

print("___MULTIPLICATION___")
def mul(a,b):
    mul=a*b
    print (f"the Multiplication value is {mul}\n")
mul(int(input("Enter a value: ")),int(input("Enter b value: ")))

print("___DIVISION___")
def div(a,b):
    div=a/b
    print (f"the Division value is {div}\n")
div(int(input("Enter a value: ")),int(input("Enter b value: ")))

print("___MODULES___")
def mod(a,b):
    mod=a%b
    print (f"the Modules value is {mod}\n")
mod(int(input("Enter a value: ")),int(input("Enter b value: ")))

print("___FLOOR DIVISION___")
def fdiv(a,b):
    fdiv=a//b
    print(f"the floor_division value is {fdiv}\n")
fdiv(int(input("Enter a value: ")),int(input("Enter b value: ")))

print("___EXPONENTIAL___")
def expo(a,b):
    expo=a^b
    print (f"the Exponential value is {expo}\n")
expo(int(input("Enter a value: ")),int(input("Enter b value: ")))
