x = 6
y = 8

while y != 0 :
    temp = x&y
    x = x^y
    y=temp<<1
print(x)