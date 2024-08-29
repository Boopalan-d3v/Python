start = int(input("Enter the Starting Number :"))
end = int(input("Enter the Ending nuber :"))

for num in range (start, end +1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0 :
                break
        else:
            print(num)