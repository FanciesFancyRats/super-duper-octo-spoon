def f1(x):
    def g():
        x = 'abc'
        #assert False
        print 'x =', x
    x = x + 1
    print 'x =', x
    g()
    return x
x = 3
z = f1(x)
