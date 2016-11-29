#-*- coding: utf-8 -*-

def const(a):
    return lambda x: a

def compose(f, g):
    def f_g(*a):
        return f(g(*a))
    return f_g

def id(*a):
    if len(a) == 1:
        return a[0]
    else:
        return a


def test():
    print "Begin tests:"

    pr = lambda x, y: lambda f: f(x)+f(y)

    pr11 = pr(1,1)
    print pr11(id)

    print "Tests ended."

if __name__ == "__main__":
    test()

