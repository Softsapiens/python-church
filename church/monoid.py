# -*- coding: utf-8 -*-

import church.fhelper as fh

# (a -> r) -> r -> (r -> r -> r) -> r
def monoid(mempty, mpure, mappend):
    pass

def mempty():
    return lambda e, p, a: e

def mpure(v):
    return lambda e, p, a: p(v)

def mappend(m1, m2):
    return lambda e, p, a: a(m1(e, p, a), m2(e, p, a))


def test():
    print "Begin tests:"

    mops = mappend(mappend(mpure(1), mpure(2)), mempty())

    print mops("0", lambda x: str(x), lambda x, y: x + '+' + y)
    print mops(0, fh.id, lambda x, y: x+y)

    print "End tests."

if __name__ == "__main__":
    test()
