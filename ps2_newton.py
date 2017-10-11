# 6.00 Problem Set 2
#
# Successive Approximation
#
def evaluate_poly(poly, x):
    guess = x
    guess = float(guess)
    poly = map(float, poly.split())
    terms = len(poly)
    terms = int(terms)
    count = 0
    count = int(count)
    ans = 0
    ans = int(ans)

    while (count < terms):
     print(count) ,
     print(' < ') ,
     print(terms)
     poly[count] = (poly[count] * (guess**count))
     ans = ans + poly[count]
     count = count + 1

    return(ans)

def compute_deriv(poly):
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
    del poly[0]
    #do I need this? first term will always be 0. 
    print(poly)
    return(poly)
poly = '-13.39 2.0 17.5 3.0 1.0'
polyderi = compute_deriv(poly)
print(polyderi)
#    """
#    Computes and returns the derivative of a polynomial function. If the
#    derivative is 0, returns (0.0,).
#
#    Example:
#    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
#    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
#    (0.0, 35.0, 9.0, 4.0)
#
#    poly: tuple of numbers, length > 0
#    returns: tuple of numbers
#    """
#    # TO DO ...

#def compute_root(poly, x_0, epsilon):
#    """
#    Uses Newton's method to find and return a root of a polynomial function.
#    Returns a tuple containing the root and the number of iterations required
#    to get to the root.

#    Example:
#    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
#    >>> x_0 = 0.1
#    >>> epsilon = .0001
#    >>> print compute_root(poly, x_0, epsilon)
#    (0.80679075379635201, 8.0)
#
#    poly: tuple of numbers, length > 1.
#         Represents a polynomial function containing at least one real root.
#         The derivative of this polynomial function at x_0 is not 0.
#    x_0: float
#    epsilon: float > 0
#    returns: tuple (float, int)
#    """
#    # TO DO ...
