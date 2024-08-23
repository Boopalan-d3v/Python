# How do you find the duplicate number on a given integer array?

def duplicate(mArr):
    size = len(mArr)
    repeated = []
    for i in range (size):
        k= i + 1
        for j in range (k , size):
            if mArr[i] == mArr[j]  and mArr[i] not in repeated:
                repeated.append(mArr[i])  
    return repeated
mArr = [3,4,1,7,7,8,4]
print(duplicate(mArr))

# Another method without using function

myArray = [1, 2, 3, 4, 8,4, 3, 5, 1, 6, 8]
unique = []
duplicate = []

for i in myArray:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(duplicate)