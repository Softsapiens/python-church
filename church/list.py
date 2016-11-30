#-*- coding: utf-8 -*-

import church.maybe as maybe

# Data List a = Nil | Cons Nil (List a)
# List Church encoding as r -> (a->b->r) -> r
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
    if isNil(l):
        return 0
    else:
        return 1 + len(tail(l))

def append(l, v):
    if isNil(l):
        return cons(v, nil())
    else:
        return cons(maybe.fromJust(head(l)), append(tail(l), v))

def reverse(l):
    if isNil(l):
        return l
    else:
        return append(reverse(tail(l)), maybe.fromJust(head(l)))

# TODO: abstract over a fold
def to_str(l):
    if isNil(l):
        return "NIL"
    else:
        return str(maybe.fromJust(head(l))) + ":" + to_str(tail(l))

# Functor instance
def map(f, l):
    return lambda n, c: l(n, lambda a, b: c(f(a), map(f, b)))

def map2(f, l):
    if isNil(l):
        return l
    else:
        return cons(f(maybe.fromJust(head(l))), map(f, tail(l)))

def test():
    NIL = nil()
    l = cons(1, cons(2, NIL))

    print isNil(l)
    print isNil(NIL)

    print maybe.fromJust(head(tail(l)))

    print to_str(l)

    lp = append(l, 3)
    print to_str(lp)

    lr = reverse(lp)

    print to_str(lr)

    lpadd1 = map(lambda x: x+1, lp)
    print to_str(lpadd1)
    lpadd1_ = map2(lambda x: x+1, lp)
    print to_str(lpadd1_)


if __name__ == "__main__":
    # Examplification use case
    test()
