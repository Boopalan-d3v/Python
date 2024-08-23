# How do you find the missing number in a given integer array of 1 to 100?

myArray = [1,2,3,100]
missing_Element = []
for i in range (myArray[0], myArray[-1]+1):
    if i not in myArray:
        missing_Element.append(i)
print(missing_Element)