x = int(raw_input('enter an integer: :'))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    print 'current guess is' , ans

print 'last guess was ', ans
print 'ans*ans*ans', ans*ans*ans

if(ans*ans*ans == abs(x)):
    if (x < 0):
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
else:
    print x, 'is not a perfect cube'
#if ans*ans*ans != abs(x):
#    print x, 'is not a perfect cube'
#elif x < 0:
#    print 'Negative int entered'
#    ans = -ans    
#print 'Cube root of ' + str(x) + ' is ' + str(ans)
