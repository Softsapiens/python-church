#-*- coding: utf-8 -*-

# Maybe Church encoding as r -> (a->r) -> r
def nothing():
    return (lambda x, y: x)

def just(a):
    return (lambda x, y: y(a))

def fromJust(m):
    return m(ValueError("Error: Nothing instance"), lambda x: x)

def isNothing(m):
    return m(True, lambda x: False)

def isJust(m):
    return m(False, lambda x: True)

def to_str(m):
    if isNothing(m):
        return 'Nothing'
    else:
        return 'Just({})'.format(fromJust(m))

# Functor instance
def map(f, m):
    if isNothing(m):
        return m
    else:
        return just(f(fromJust(m)))

if __name__ == "__main__":
    # Examplification use case

    n = nothing()
    j2 = just(2)

    assert(isNothing(j2)==False)
    assert(to_str(j2)=='Just(2)')
    assert(isNothing(n)==True)

    print to_str(j2) # --> 2
    print to_str(n) # --> Exception

