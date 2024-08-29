val = int(input("Enter the value :"))
factorial = 1
if val < 0:
    print("Please Enter positive Integer !")
elif (val == 0):
    print(f"The factorial of {val} is 1")
else:
    for i in range(1, val+1):
        factorial = factorial * i
    print(f'The factorial of {val} is : {factorial}')
