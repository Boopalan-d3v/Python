str = input("Enter the string :").lower()
chr = input("Enter the charecter you want to count :").lower()
count = 0

for i in str:
    if i == chr:
        count +=1
print(count)

#Another method to count character
#Using count() method

print(str.count(chr))