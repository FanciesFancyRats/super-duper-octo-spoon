l = 8
w = 8
x = 1
y = 1
z = 0
a = 0
b = 0
count = 0

while (z <= 8):
    print('x, y')
    print(x)
    print(y)
    print(z)
    a = w - z
    b = l - z
    if (((x + z) <= w) and ((y + z) <= l)):
        x = x + 1
        print(' x is :')
        print(x)
        count = count + 1
        print(count)
    if ((x + z) > 8):
        print('line 18')
        x = 1
        y = y + 1
    if ((y + z) > 8):
        print('line 19')
        z = z + 1
        y = 1
        x = 1
print('*** Solved ***')
print(count)
