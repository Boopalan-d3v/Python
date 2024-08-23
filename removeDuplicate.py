hello = [1, 2, 3, 1, 4, 5, 2]
print(list(set(hello)))

# Remove the items that are duplicated in two lists 

hell = [3, 4, 7, 2, 2, 1]
world = [9, 8, 8, 7]
print(list(set(hell) ^ set(world)))

# Without arrenging in ascending order 

def Remove(duplicate):
    final = []
    for num in duplicate:
        if  num not in final:
            final.append(num)
    return final
duplicate = [2,3,1,4,1,6,7,4,2,1,9,0]
print(Remove(duplicate))