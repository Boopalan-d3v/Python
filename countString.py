para=["A", "good", "example", "of", "a", "paragraph", "contains" ,"a" 
,"topic" ,"sentence", "details" ,"and", "a", "conclusion",
"There", "are", "many", "different", "kinds", "of", "animals", "that" ,"live", "in", "China", 
"Tigers","and","leopards","are","animals","that","live","in","China","forests","in","the", "north"]

one=[]      #create a empty list to add items
two=[]
three=[]
four=[]
five=[]
six=[]
seven=[]
eight=[]
nine=[]
ten=[]

for i in para:      #To check each item lenght in list
    if len(i)==1:   #To check length of item is = 1
        one.insert(0,i) #here we insert fun() to insert the item here 0 is position and i is item
    if len(i)==2:
        two.append(i)   #Here we use append() to insert item into the list
    if len(i)==3:
        three.append(i)
    if len(i)==4:
        four.append(i)
    if len(i)==5:
        five.append(i)
    if len(i)==6:
        six.append(i)
    if len(i)==7:
        seven.append(i)
    if len(i)==8:
        eight.append(i)
    if len(i)==9:
        nine.append(i)
    if len(i)==10:
        ten.append(i)
        
print(one)  #To print the list one
ol=len(one) #store the length of the list one
print(f"the length of 1 letter list is {ol}\n") #To display the lenght of one using fString

print(two)
tl=len(two)
print(f"the length of 2 letter list {tl}\n")

print(three)
thl=len(three)
print(f"the length of 3 letter list {thl}\n")

print(four)
fl=len(four)
print(f"the length of 4 letter list {fl}\n")

print(five)
fvl=len(five)
print(f"the length of 5 letter list {fvl}\n")

print(six)
sl=len(six)
print(f"the length of 6 letter list {sl}\n")

print(seven)
sel=len(seven)
print(f"the length of 7 letter list {sel}\n")

print(eight)
el=len(eight)
print(f"the length of 8 letter list {el}\n")

print(nine)
nl=len(nine)
print(f"the length of 9 letter list {nl}\n")

print(ten)
tel=len(ten)
print(f"the length of 10 letter list {tel}\n")
