# 6.00 Problem Set 2
#
# Successive Approximation
#
s = raw_input('Please enter a polynomial seperated by commas: ')
poly = map(float, s.split())
print(poly)
x = 0
y = 0
place = 0
totalXs = len(poly)
xTo0 = poly[0]
xTo1 = poly[1]
xTo2 = poly[2]
xTo3 = poly[3]
xTo4 = poly[4]
guess = 0
guess = float(guess)
ans = 0
rx = 0
lx = 0
count = 0

working = ((xTo0) + (xTo1 * rx) + (xTo2 * (rx**2)) + (xTo3 * (rx**3)) + (xTo4 * (rx**4)))
print(working)
#while
#while (x < 99):
 #working = ((xTo0) + (xTo1 * guess) + (xTo2 * (guess**2)) + (xTo3 * (guess**3)) + (xTo4 * (guess**4)))

 #print(xTo0) ,
 #print(xTo1 * guess) ,
 #print(xTo2 * guess**2) ,
 #print(xTo3 * guess**3) ,
 #print(xTo4 * guess**4)
 #print(working)
 #working = round(working, 2)
 #x = x + 1
 #print(guess) ,
 #print(',') ,

 #print(working)


 #if (working == 0):
  #print('****')
  #print(guess)
  #ans = guess
 #guess = guess + 0.1
#print(ans)

#def evaluate_poly(poly, x):
#    """
#   Computes the polynomial function for a given value x. Returns that value.
#
#    Example:
#    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
#    >>> x = -13
#    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
#    180339.9
#
#    poly: tuple of numbers, length > 0
#    x: number
#    returns: float
#    """
    # TO DO ...
#
#
#def compute_deriv(poly):
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
