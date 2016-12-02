#-*- coding: utf-8 -*-

import church.maybe as maybe

# Data List a = Nil | Cons Nil (List a)
# List Church encoding as r -> (a->b->r) -> r
def _list(n, c):
    pass

def nil():
    return (lambda x, y: x)

def cons(a, b):
    return (lambda x, y: y(a, b))

def isNil(l):
    return l(True, lambda x, y: False)

def head(l):
    return l(maybe.nothing(), lambda x, y: maybe.just(x))

def tail(l):
    return l(Exception("Error: Nil list"), lambda x, y: y)

def len(l):
    return l(0, lambda h, t: 1 + len(t))

def append(l, v):
    if isNil(l):
        return cons(v, l)
    else:
        return lambda n, c: l(n, lambda h, t: c(h, append(t, v)))

def reverse(l):
    if isNil(l):
        return l
    else:
        return append(reverse(tail(l)), maybe.fromJust(head(l)))

def to_str(l):
    return l("NIL", lambda h, t: str(h) + ":" + to_str(t))

# Functor instance
def map(f, l):
    return lambda n, c: l(n, lambda a, b: c(f(a), map(f, b)))

def map2(f, l):
    if isNil(l):
        return l
    else:
        return cons(f(maybe.fromJust(head(l))), map(f, tail(l)))

def test():
    print "Begin tests:"

    NIL = nil()
    l = cons(1, cons(2, NIL))

    print isNil(l)
    print isNil(NIL)

    print "NIL list -> " + to_str(NIL)
    print "l-> " + to_str(l)
    print "head(tail(l))-> " + str(maybe.fromJust(head(tail(l))))

    np = append(NIL, 'a')
    print "append a to NIL -> " + to_str(np)

    lp = append(append(l, 3), 4)
    print "append 3 & append 4  to l -> " + to_str(lp)

    lr = reverse(lp)
    print "reversed -> " + to_str(lr)

    lpadd1 = map(lambda x: x+1, lp)
    print "church map(adding 1) encoding-> " + to_str(lpadd1)
    lpadd1_ = map2(lambda x: x+1, lp)
    print "recursive map(adding 1)-> " + to_str(lpadd1_)

    print "End tests."


if __name__ == "__main__":
    # Examplification use case
    test()
