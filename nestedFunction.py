print("______Arithmetic operations_____\n")

def air(a,b): # global variable declaration
    def add(): #Function within another function
        add=a+b #gets the value from main function
        print(f"the addition value is {add}\n")
    add()

    def sub(): #second sub fun()
        sub=a-b
        print(f"the subraction value is {sub}\n")
    sub()

    def mul():  #third sub fun()
        mul=a*b
        print(f"the Multiplication value is {mul}\n")
    mul()

    def div():  #fourth sub fun()
        div=a/b
        print(f"the division value is {div}\n")
    div()

    def mod(): #fifth sub fun()
        mod=a%b #modules operation
        print(f"the Module value is {mod}\n")
    mod()

    def fdiv(): #sixth sub fun()
        fdiv=a//b   #floor division operation
        print(f"the floor division value is {fdiv}\n")
    fdiv()

    def exp():  #seventh sub fun()
        exp=a^b #exponential operation
        print(f"the exponential value is {exp}\n")
    exp()


air(int(input("Enter a value: ")),int(input("Enter b value: "))) #Assigns values to the Main function


