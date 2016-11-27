

# Maybe Church encoding as r -> (a->r) -> r
def nothing():
    return (lambda x, y: x)

def just(a):
    return (lambda x, y: y(a))

def fromJust(m):
    return m(Exception("Error: Nothing instance"), lambda x: x)

def isNothing(m):
    return m(True, lambda x: False)

def isJust(m):
    return m(False, lambda x: True)

if __name__ == "__main__":
    # Examplification use case

    n = nothing()
    j2 = just(2)

    print fromJust(j2) # --> 2
    print fromJust(n) # --> Exception

    print isNothing(n)
    print isNothing(j2)

