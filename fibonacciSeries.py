val = int(input("Enter the value :")); #Get the input value
n1,n2 = 0,1;
count = 0 ;

if(val <= n1):
    print("please Enter the positive Integer");
elif(val == n2):
    print(f"the fibonacci value of {val} is : {n1}");
else:
    print("The Fibonacci series are");
    while(count < val):
        print(n1);
        x = n1 + n2 ;
        n1 = n2;
        n2 = x;
        count += 1; #increment of count example "count = count + 1"
