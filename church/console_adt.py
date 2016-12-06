#-*- coding: utf-8 -*-

# console :: (()->r) -> (a -> r) -> r
def read():
    return lambda r, w: r()
def write(s):
    return lambda r, w: w(s)

def flatmap(c, fnext):
    return lambda r, w: fnext(c(r, w))(r, w)

def map(f, c):
    return lambda r, w: c(lambda: f(r()), lambda s: w(f(s)))

def test():
    print "Begin tests."

    def _write(s):
        print s

    def _memread(words):
        # removes and returns the last element of the list
        return lambda: words.pop()

    r1 = read()
    print map(lambda s: s.upper(), r1)(lambda: "upper mapped reading test", None)

    w1 = write("upper mapped writing test")
    map(lambda s: s.upper(), w1)(None, _write)

    prog = flatmap(read(), lambda s: write(s))
    map(lambda s: s.upper(), prog)(lambda: "upper mapped flatmaping test", _write)

    hoprog = flatmap(read(), lambda s: flatmap(read(), lambda s1: write(s + " " + s1)))
    hoprog(_memread(["this not gonna happen", "guys", "Hi"]), _write)

    print "Tests ended."

if __name__ == "__main__":
    # Examplification use case
    test()
