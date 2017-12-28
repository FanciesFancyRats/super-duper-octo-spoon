#approximation - how good of an approximation are we willing to accept?
#Find a y s.t. y*y = x +/- tolerance
x = raw_input('enter a number: ')
x = int(x)
epsilon = 0.01
numGuesses = 0
ans = 0.0
while abs(ans - x) >= epsilon and ans <= x:
    ans += 0.0001
    numGuesses += 1
if abs(ans - x) >= epsilon:
    print 'could not find a value'
else:
    print ans, 'is close to ', x
