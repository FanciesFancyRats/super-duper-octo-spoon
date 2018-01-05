#approximation - how good of an approximation are we willing to accept?
#Find a y s.t. y*y = x +/- tolerance
#x = raw_input('enter a number: ')
#x = float(x)
#epsilon = 0.01
#numGuesses = 0
#ans = 0.0
#while abs(ans**2 - x) >= epsilon and ans <= x:
#    ans += 0.0001
#    #print ans
#    numGuesses += 1
#print 'Number of guesses: ' , numGuesses
#if abs(ans**2 - x) >= epsilon:
#    print 'could not find a value'
#else:
#    print ans, 'is close to ', x
x = raw_input('enter a number: ')
x = float(x)

epsilion = 0.01
epsilion = float(epsilion)
numGuesses = 0
low = 0.0
high = max(x, 1.0)

print 'type(x) ', type(x)
print 'type(epsilion)', type(epsilion)
print 'type(numGuesses)', type(numGuesses)
print 'type(low)', type(low)
print 'type(high)', type(high)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilion and ans <=x:
    print low, high, ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'Number of guesses: ', numGuesses
print ans, 'is close to square root of' , x
