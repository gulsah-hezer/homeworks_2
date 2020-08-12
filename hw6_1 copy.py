#1. (50 pts) Consider the finite field F3409573 and the elliptic curve E : y2 = x3 + 723x + 4096.
# Apply Hasse-Weil bound to find the order of E(F3409573). Note that (0,64) is on the curve.
# Discuss the number of elements in E[3], E[5], E[7], E[11]. Find elements in E(F3409573) whose orders are 11 and 309989.


import collections


def inv(n, q):
    """div on PN modulo a/b mod q as a * inv(b, q) mod q
    >>> assert n * inv(n, q) % q == 1
    """
    return pow(n, -1, q)


def sqrt(n, q):
    """sqrt on PN modulo: it may not exist
    >>> assert (sqrt(n, q) ** 2) % q == n
    """
    assert n < q
    for i in range(1, q):
        if i * i % q == n:
            return (i, q - i)
        pass
    raise Exception("not found")


Coord = collections.namedtuple("Coord", ["x", "y"])


class EC(object):
    """System of Elliptic Curve"""
    def __init__(self, a, b, q):
        """elliptic curve as: (y**2 = x**3 + a * x + b) mod q
        - a, b: params of curve formula
        - q: prime number
        """
        assert 0 < a and a < q and 0 < b and b < q and q > 2
        assert (4 * (a ** 3) + 27 * (b ** 2))  % q != 0
        self.a = a
        self.b = b
        self.q = q
        # just as unique ZERO value representation for "add": (not on curve)
        self.zero = Coord(0, 0)
        pass

    def is_valid(self, p):
        if p == self.zero: return True
        l = (p.y ** 2) % self.q
        r = ((p.x ** 3) + self.a * p.x + self.b) % self.q
        return l == r

    def at(self, x):
        """find points on curve at x
        - x: int < q
        - returns: ((x, y), (x,-y)) or not found exception
        >>> a, ma = ec.at(x)
        >>> assert a.x == ma.x and a.x == x
        >>> assert a.x == ma.x and a.x == x
        >>> assert ec.neg(a) == ma
        >>> assert ec.is_valid(a) and ec.is_valid(ma)
        """
        assert x < self.q
        ysq = (x ** 3 + self.a * x + self.b) % self.q
        y, my = sqrt(ysq, self.q)
        return Coord(x, y), Coord(x, my)

    def neg(self, p):
        """negate p
        >>> assert ec.is_valid(ec.neg(p))
        """
        return Coord(p.x, -p.y % self.q)

    def add(self, p1, p2):
        """<add> of elliptic curve: negate of 3rd cross point of (p1,p2) line
        >>>  c = ec.add(a, b)
        >>> assert ec.is_valid(a)
        >>> assert ec.add(c, ec.neg(b)) == a
        """
        if p1 == self.zero: return p2
        if p2 == self.zero: return p1
        if p1.x == p2.x and p1.y != p2.y:
            # p1 + -p1 == 0
            return self.zero
        if p1.x == p2.x:
            # p1 + p1: use tangent line of p1 as (p1,p1) line
            l = (3 * p1.x * p1.x + self.a) * inv(2 * p1.y, self.q) % self.q
            pass
        else:
            l = (p2.y - p1.y) * inv(p2.x - p1.x, self.q) % self.q
            pass
        x = (l * l - p1.x - p2.x) % self.q
        y = (l * (p1.x - x) - p1.y) % self.q
        return Coord(x, y)

    def mul(self, p, n):
        """n times <mul> of elliptic curve
        >>> m = ec.mul(n, p)
        >>> assert ec.is_valid(m)
        """
        r = self.zero
        for i in range(n):
            r = self.add(r, p)
            pass
        return r
    pass

#______________________SONUÇ__________________________
print('Please wait 1 second to have an answer...')



def double_and_add(n, g):
    """
    Returns the result of n * x, computed using
    the double and add algorithm.
    """
    result = Coord(0,0)
    addend = g
    i=21
    E1 = EC(723,4096,3409573)
    for[int(d) for d in bin(n)[2:].zfill(8)][i] in [int(d) for d in bin(n)[2:].zfill(8)]:
        if [int(d) for d in bin(n)[2:].zfill(8)][i]== 1:
            result = E1.add(result,addend)
        addend =E1.add(addend,addend)
        i = i - 1
    return result



for n in range(3405880,3413267):
    #print(n)
    double_and_add(n, Coord(0, 64))
    if double_and_add(n, Coord(0, 64))==(0,0):
           print(double_and_add(n, Coord(0, 64)))
           print('ORDER of first curve İS:',n)
    n=n+1


E1=EC(723,4096,3409573)
print('1.POİNT İS:',E1.mul(Coord(0, 64),22))
print('2.POİNT İS:',E1.mul(Coord(54641, 300305),11))

print(E1.at(1))







