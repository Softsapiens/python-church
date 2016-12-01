#-*- coding: utf-8 -*-

import church.fhelper as fh

# Maybe Church encoding as r -> (a->r) -> r

def _maybe(n, j):
    pass

def nothing():
    return (lambda x, y: x)

def just(a):
    return (lambda x, y: y(a))

def fromJust(m):
    return m(ValueError("Error: Nothing instance"), fh.id)

def isNothing(m):
    return m(True, lambda x: False)

def isJust(m):
    return m(False, lambda x: True)

def to_str(m):
     return m('Nothing', lambda a: 'Just({})'.format(a))

# Functor instance
def map(f, m):
    return lambda n, j: m(n, lambda a: f(a))

def test():
    print "Begin tests:"
    n = nothing()
    j2 = just(2)

    assert(isNothing(j2)==False)
    assert(to_str(j2)=='Just(2)')
    assert(isNothing(n)==True)

    print to_str(j2) # --> 2
    print to_str(n) # --> Nothing

    j3 = map(lambda v: v+1, j2)
    print to_str(j3)

    print to_str(map(lambda v: v+1, n))

    print "End tests."

if __name__ == "__main__":
    # Examplification use case
    test()

