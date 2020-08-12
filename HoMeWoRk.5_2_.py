# Consider the elliptic curve E : y2 = x3 + 1811x + 2018 over the finite field F54877. Consider the point
#P = (2, 23969) on the curve E. Using Hasse-Weil bound, find the order of P. Then find at least 5 points on the curve
#whose orders are exactly 13723.
import collections


def inv(n, q):
    """div on P N modulo a/b mod q as a * inv(b, q) mod q
    >>> assert n * inv(n, q) % q == 1
    """
    for i in range(q):
        if (n * i) % q == 1:
            return i
        pass
    assert False, "unreached"
    pass


def sqrt(n, q):
    """sqrt on P N modulo: it may not exist
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
#****************************************************_SONUÇ_*************************************************************
#INTERVAL BULMA(HASSE WEİL BOUND):

import math

a1=-(2*math.sqrt(54877))+(54877)+1
print(math.floor(a1))
a2=(2*math.sqrt(54877))+(54877)+1
print(math.floor(a2))

E2=EC(1811,2018 ,54877)


print('please wait some to have an answer...')

def double_and_add(n, g):
    """
    Returns the result of n * x, computed using
    the double and add algorithm.
    """
    result = Coord(0,0)
    addend = g
    i=15
    E2 = EC(1811,  2018 , 54877)
    for[int(d) for d in bin(n)[2:].zfill(8)][i] in [int(d) for d in bin(n)[2:].zfill(8)]:
        if [int(d) for d in bin(n)[2:].zfill(8)][i]== 1:
            result = E2.add(result,addend)
        addend =E2.add(addend,addend)
        i = i - 1
    return result



for n in range(54409,55346):
    #print(n)
    double_and_add(n, Coord(2, 23969))
    if double_and_add(n, Coord(2, 23969))==(0,0):
           print(double_and_add(n, Coord(2, 23969)))
           print('ORDER İS:',n)
    n=n+1

# we have a conclusion: order of curve is 54892. BUT MAY BE POİNT P = (2, 23969)  HAS A SMALLER ORDER
# THAN ORDER OF CURVE. THEN we need to make test if it is or not.IS THERE AN EASY WAY TO CALCULATE, I dont know.
#THANKFULLY, we  have really  few prime factors of it.then we can try :)
#54892=2*2*13723

print(E2.mul(Coord(2, 23969),2))#=(x=3279, y=42738)
print(E2.mul(Coord(2, 23969),4))#=(x=4371, y=15530)
print(E2.mul(Coord(2, 23969),13723))#=(x=5112, y=0)
print(E2.mul(Coord(2, 23969), 27446))#=(0,0)
print(E2.mul(Coord(2, 23969), 54892))#=(0,0)

#WE UNDERSTAND THAT POİNT (2, 23969) HAS ORDER 54892.

#şimdi 5 tane point  bulacağız order ı 13723 olan yani bu ne demek 13723.p=(0,0)
# biz sonuçta 1 tane nokta biliyoruz (2, 23969)*54892=(0,0) o zaman (2, 23969)*4 is our fisrt point that have order 13723.
#YANİ 4P*13723=(0,0)


#*******1.POİNT:
print('1.POİNT İS:',E2.mul(Coord(2, 23969), 4))#=Coord(x=4371, y=15530)
#*******2.POİNT:
print('2.POİNT İS:',E2.mul(Coord(4371, 15530),2))#=Coord(x=15768, y=11022)
print(E2.at(15768))
#*******3.POİNT:
print('3.POİNT İS:',E2.mul(Coord(15768,11022), 2))#=Coord(x=27024, y=19569)
#*******4.POİNT:
print('4.POİNT İS:',E2.mul(Coord(27024, 19569), 2))#=Coord(x=15477, y=26676)
#*******5.POİNT:
print('5.POİNT İS:',E2.mul(Coord(x=15477, y=26676), 2))#= Coord(x=5426, y=39493)






