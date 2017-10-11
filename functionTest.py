def add2(x, y):
    z = (x + y)
    print(x) ,
    print(' + ') ,
    print(y) ,
    print(' = ') ,
    print(z)
    return(z)
number = raw_input('Input a number: ')
number = int(number)
number2 = raw_input('Input another number: ')
number2 = int(number2)
number = add2(number, number2)
print(number)
