s = raw_input('Please enter a polynomial seperated by commas: ')
poly = map(float, s.split())
guess = raw_input('Please enter an x value: ')
guess = float(guess)
numberXs = len(poly)
count = 0
count = int(count)
ans = 0
if (numberXs > 0):
 while(count < numberXs):
  print(count)
  ans = ans + ((poly[count]) * (guess**(count)))
  count = count + 1
print(numberXs)
print(ans)
