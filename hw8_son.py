import math
#1. aşama:**************************************************************************************************************
q=int(input('*IN THIS CODE WE ARE TESTING PRIMALITY OF İNETEGER N,please enter integers suct that n> 1002:'))
if q> 1002:
    print('*you entered it correctly and your integer n is:',q)
else:
    print('*you are supposed to enter integers s.t.n> 1002')

#2.aşama:we need to find prime p larger than 2(n^1/4+1)^2***************************************************************
def finding_prime(q):
      if q > 1002:
          m=q**(1/4)
          g=(m+1)
          s = math.ceil((2*(g**2)))
          while  (s>g):
              for x in range(2,s):
                   if s%x==0:
                       break
                   else:
                       print('*your prime number p larger than 2(n^1/4+1)^2:',s)
                       return(s)
              s=s+1

s=finding_prime(q)

#3.aşama: finding k such that k=p*x(i.e. p divides k)
#at the same time, k satisfies eqn s.t. n+1-2kökn<= k<=n+1+2kökn********************************************************

n1 = int(q + 1 - 2 * math.sqrt(q))
n2 = int(q + 1 + 2 * math.sqrt(q))

def finding_k(q,s):
    if q > 1002:
        n1=q+1-2*math.sqrt(q)
        n2=q+1+2*math.sqrt(q)
        print('*your lower bound of hasse weil:',n1)
        print('*your upper bound of hasse weil:',n2)
        m1=int(n1/s)
        m2=int(n2/s)
        print('*your lower bound after dividing by prime number p:',m1)
        print('*your upper bound after dividing by prime number p:',m2)
        for x in range(m1,m2+1):
            if (m2+1)-m1==3:
                x=(m1+m2)/2
                print('*your k s.t. k=p*x and satisfies hasse bound property is:',int(x*s))
                k=(x*s)
                break
            elif (m2+1)-m1==2:
                x=m2
                print('*your k s.t. k=p*x and satisfies hasse bound property is:', int(x * s))
                k = (x * s)
                break
        return(int(x*s))

k=finding_k(q,s)
####*AND THE LAST STEP**************************************************************************************************

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
    def __init__(self, a,b, q):
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

#*****************************************************C O N C L U S I O N ***********************************************
#bu aşamada aynı structure da verilen fakat farklı pointleri içeren (0,a) elliptic curve için girdiğimiz n
#bilgisine göre oluşturduğumuz  p ve k verisine göre k ÇARPI bu noktanın identity vermesi ve p ye bölümünün
#vermediği bir noktayı bulabildiğimiz takdirde a yı yazdırıyoruz.


def prime_mı_testi_ve_check_identity(q):
    if q > 1002:
        for a in range(2,q):
            b = (a ** 2) % q
            if (4 * (a ** 3) + 27 * (b ** 2)) % q != 0:
                E1=EC(a,(a**2)%q,q)
                print('a:',a)
                if E1.mul(Coord(0,a),k)==Coord(0,0) and E1.mul(Coord(0,a),int(k/s))!=Coord(0,0) :
                    print('*for this a:',a,'we have reached identity s.t.',E1.mul(Coord(0,a),k))
                    print('*this implies that this n:',q,'is prime integer.')
                    return(a)
                pass
            else:
                return(0)





#şimdi burada yapmak istediğim belirlediğimiz q ya giderken kaçıncı aşamada inverse yi bulamadığımızı araştırmak ;)
#şimdi mesala örneğin 10231=13*787, bunun için biz a için hangi değeri alırsak alalım multiplication ı yaparken
# x2-x1 in 13 olduğu durumda ne olacak ? inverse yi bulaammaaayacak ooo.Ve biz anlayacaz ki composite mişşş.Şimdi
# burada (0,a) yı eklediğimiz için ve multiplication add ile oluştuğu için 0 ı bir önceki x2 den çıkarmış oluyoruz.
# bu durumda 13 çarpanını içeriyorsa önceki x2 biz stop ediyoruz :)

#E1=EC(2,(2**2)%10231,10231)
#print(E1.mul(Coord(0, 2), 16))


def composite_mi_testi_2(q):
    if q > 1002:
        for a in range(2, q):
            b = (a ** 2) % q
            if (4 * (a ** 3) + 27 * (b ** 2)) % q != 0:
                    E1 = EC(a, (a ** 2) % q, q)
                    if  math.gcd(2 *a, q)!=1:
                        for i in range(2, int(k / s) + 1):
                            E2 = EC(a, (a ** 2) % int(k / s), int(k / s))
                            print('a:', a)
                            print('i:', i)
                            print('factor is found and it is', math.gcd(2 *a, q))
                            print('*this implies that this n:', q, 'is composite number.It has factor:',math.gcd(2 *a, q))
                            if E2.mul(Coord(0, a), i) == Coord(0, 0):
                                print('*for this a:', a, 'and i:', i + 1, ',we have reached identity s.t.',
                                E2.mul(Coord(0, a), i + 1))
                                break
                            return(0)
                    elif E1.mul(Coord(0, a), k) == Coord(0, 0) and E1.mul(Coord(0, a), int(k / s)) != Coord(0, 0):
                        print('*for this a:', a, 'we have reached identity s.t.', E1.mul(Coord(0, a), k))
                        print('*this implies that this n:', q, 'is prime integer.')
                        return (a)
                    else:
                        for i in range(2, int(k / s) + 1):
                            x = E1.mul(Coord(0, a), i)[0]
                            if  x!=0 and math.gcd(x,q)!=1 and x!=q  and math.gcd(x,q)!=q:
                                print('a:', a)
                                print('i:',i)
                                print('factor is found and it is:',math.gcd(x,q))
                                E2 = EC(a, (a ** 2) % int(k/s), int(k/s))
                                print('*this implies that this n:', q, 'is composite number.It has factor:',math.gcd(x,q))
                                if E2.mul(Coord(0, a), i+1) == Coord(0, 0):
                                    print('*for this a:', a,'and i:',i+1,',we have reached identity s.t.', E2.mul(Coord(0, a),i+1))
                                    print('*this implies that this n:', q, 'is composite number.')
                                    return(0)




#iki farklı test için tek bir fonksiyon oluşturamadım dolayısıyla ilk composite olup olmadığını test ediyor ve sonra
#prime olduğunu söylemek ve istenilen a yı bulmak için program çalışıyor. Bu durumda da maalesef kodumuz çok ama çok
# yavaş çalılışıyor, dolayısıyla cevap için beklememiz gerekiyor :/

composite_mi_testi_2(q)



