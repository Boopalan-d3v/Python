x = 6
y = 8

while y != 0 : #checking y not equal to 0 condition: True
    temp = x&y #concat x & y and store on temp
    x = x^y 
    y=temp<<1
print(x)