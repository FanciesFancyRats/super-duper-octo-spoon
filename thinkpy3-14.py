def check_fermat(a, b, c, n):
    if(a^n + b^n) == (c):
       print("Holy smokes, Fermat was wrong!")
    else:
       print("Fermat was right")
a = raw_input("a =")
b = raw_input("b =")
c = raw_input("c =")
n = raw_input("n =")
a = int(a)
b = int(b)
c = int(c)
n = int(n)
check_fermat(a, b, c, n)
