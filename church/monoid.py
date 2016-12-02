# -*- coding: utf-8 -*-

import church.fhelper as fh

# r -> (a -> r) -> (r -> r -> r) -> r
def monoid(mempty, mpure, mappend):
    pass

def mempty():
    return lambda e, p, a: e

def mpure(v):
    return lambda e, p, a: p(v)

def mappend(m1, m2):
    return lambda e, p, a: a(m1, m2)

def to_str(m):
    return traverse(m, "mempty()", lambda a: "mpure(" + str(a) + ")", lambda s1, s2: "mappend(" + s1 + ", " + s2 + ")")

def traverse(m, e, f_p, f_a):
    return m(e, f_p, lambda m1, m2: f_a(traverse(m1, e, f_p, f_a), traverse(m2, e, f_p, f_a))) 

def test():
    print "Begin tests:"

    mops = mappend(mappend(mpure(1), mpure(2)), mempty())

    print "mops -> " + to_str(mops)
    print traverse(mops, "0", lambda x: str(x), lambda x, y: x + '+' + y)
    print traverse(mops, 0, fh.id, lambda x, y: x+y)

    print "End tests."

if __name__ == "__main__":
    test()
