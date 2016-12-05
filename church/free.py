#-*- coding: utf-8 -*-

# data Free f a = Pure a
#              | Free (f (Free f a))

# liftF :: Functor f => f a -> Free f a
# liftF = Free . fmap pure

# A Functor instance for this type must traverse the entire tree:

# instance Functor f => Functor (Free f) where
#  fmap f (Pure x) = Pure (f x)
#  fmap f (Free f) = Free ((fmap f) <$> f)

# And so must (<*>) and (>>=):

# instance Functor f => Applicative (Free f) where
#  pure = Pure
#  Pure f <*> Pure x = Pure (f x)
#  Pure f <*> Free x = Free ((fmap f) <$> x)
#  Free f <*> x      = Free ((<*> x) <$> f)

# instance Functor f => Monad (Free f) where
#  return = Pure
#  Pure x >>= f = f x
#  Free x >>= f = Free ((>>= f) <$> x)

import church.fhelper as fh

# Encoding
# forall r. (a -> r) -> (f r -> r) -> r
def pure(a):
    return lambda p, f: p(a)

def free(fr):
    return lambda p, f: f(fr)

def is_pure(p):
    return p(fh.const(True), fh.const(False))

def is_free(f):
    return f(fh.const(False), fh.const(True))

# -- Church encoding of Free monad
# newtype F f a = F { runF :: forall r. (a -> r) -> (f r -> r) -> r }

# instance Functor (F f) where
    # f == (a -> b)
    # k == (fa -> fr -> r)
    # fmap f (F k) = F (\p -> k (p . f))

# instance Monad (F f) where
#    return a = F (\p _ -> p a)
#    (F k) >>= f = F (\p r -> k (\a -> runF (f a) p r) r)


# Functor instance
def map(f, fr):
    return lambda p, fr2: fr((lambda _a: p(f(_a))), fr2)


# We need f_map function in order to get the correct map over functor fa
def lift_free(f_map, fa):
    return free(f_map(lambda a: pure(a), fa))

def free_test():
    # console :: (()->r) -> (a -> r) -> r 
    def read():
        return lambda r, w: r()
    def write(s):
        return lambda r, w: w(s)

    def flatmap(c, fnext):
        return lambda r, w: fnext(c(r, w))(r, w)

    def map(f, c):
        return lambda r, w: c(f(r), lambda s: w(f(s)))

    def _write(s):
        print s

    r1 = read()
    print r1(lambda: "reading test", None)

    w1 = write("writing test")
    w1(None, _write)

    prog = flatmap(read(), lambda s: write(s))
    prog(lambda: "flatmaping test", _write)

    hoprog = flatmap(read(), lambda s1: flatmap(read(), lambda s: write(s + " " + s1)))
    def _memread(words):
        return lambda: words.pop()

    hoprog(_memread(["Hi", "guys"]), _write)

def test():
    print "Begin tests."

    p = pure("pure-case")
    f = free(fh.id)

    assert(is_pure(p) == True)
    assert(is_free(f) == True)
    assert(is_pure(f) == False)
    assert(is_free(p) == False)

    p1 = map(lambda x: x+"-mapped", p)
    print p1(fh.id, fh.id)

    f1 = map(lambda x: x+"-mapped", f)
    print is_free(f1)

    free_test()

    print "Tests ended."

if __name__ == "__main__":
    # Examplification use case
    test()
