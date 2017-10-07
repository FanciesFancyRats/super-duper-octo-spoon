poly = raw_input('Please input a polynomial: ')
poly = map(float, poly.split())
terms = len(poly)
map(float, poly)
x = 0
while (x < terms):
 if(x > 1):
  print(poly[x]) ,
  print('x') ,
  print('^') ,
  print(x) ,
  print(' + ') ,
 if(x == 1):
  print(poly[x]) ,
  print('x') ,
  print(' + ') ,
 if(x == 0):
  print(poly[x]) ,
  print(' + ')
 x = x + 1
#d/dx = nx^n-1
count = 0
while (count < terms):
 if (count == 0):
  poly[count] = 0
 if (count == 1):
  poly[count] = poly[count]
 if (count > 1):
  poly[count] = (poly[count] * count)
 count = count + 1
print(' ')
print(poly)
#make new list to get rid of extra 0
