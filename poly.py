guess = raw_input('Please input an x value: ')
guess = float(guess)
poly = raw_input('please enter a polynomial: ')
poly = map(float, poly.split())
terms = len(poly)
terms = float(terms)
count = 0
count = int(count)
ans = 0.0
while (count < terms):
 ans = (poly[count] * (guess**count))
 print(ans)
 count = count + 1