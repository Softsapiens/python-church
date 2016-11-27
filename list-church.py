
# Data List a = Nil | Cons Nil (List a)
# List Church encoding as r -> (a->b->r) -> r
def nil():
    return (lambda x, y: x)

def cons(a, b):
    return (lambda x, y: y(a, b))

def isNil(l):
    return l(True, lambda x, y: False)

def head(l):
    return l(Exception("Error: Nil list"), lambda x, y: x)

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
        return cons(head(l), append(tail(l), v))

def reverse(l):
    if isNil(l):
        return l
    else:
        return append(reverse(tail(l)), head(l))

def to_str(l):
    if isNil(l):
        return "NIL"
    else:
        return str(head(l)) + ":" + to_str(tail(l))

if __name__ == "__main__":
    # Examplification use case

    NIL = nil()
    l = cons(1, cons(2, NIL))

    print isNil(l)
    print isNil(NIL)

    print head(tail(l))

    print to_str(l)

    lp = append(l, 3)
    print to_str(lp)

    lr = reverse(lp)

    print to_str(lr)


