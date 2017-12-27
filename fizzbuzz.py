#print numbers from 1 to 100, for multiples of 3 print fizz, multiples of 5 buzz, for both fizz buzz
for i in range(100):
    if (i%3 == 0) or (i%5 == 0):
        s = ''
        if i % 3 == 0:
            s = s + 'Fizz'
        if i % 5 == 0:
            s = s + 'Buzz'
    print(s)


    
