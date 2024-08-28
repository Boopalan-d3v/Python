val = int(input('Enter the value :'))
flag = False
if val == 1:
    #print(f'{val} is not a prime number')
    flag = True
elif val > 1:
    for i in range (2, val):
        if (val % i ==0):
            flag = True
            break
if(flag):
    print(f'{val} is not prime')
else:
    print(f'{val} is prime')