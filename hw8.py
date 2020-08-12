#1. aşama:
n=int(input('please enter integers suct that n> 1002:'))
if n> 1002:
    print('you entered it correctly ')
else:
    print('you are supposed to enter integers s.t.n> 1002')

#2.aşama:we need to find prime p larger than 2(n^1/4+1)^2


def finding_prime(n):
      m=n**(1/4)
      g=2*((m+1)**2)
      print('g:',g)
      p = int(g + 1)
      while  (p>g):
          for x in range(2,p):
               if p%x==0:
                   break
               else:
                   print(p)
                   return(p)
          p=p+1

finding_prime(n)

#3.aşama: finding k such that k=p*x(i.e. p divides k)
#at the same time, k satisfies eqn s.t. n+1-2kökn<= k<=n+1+2kök

def check_identity(q,k):
    for a in range(2,q):
        E1=EC(a,a**2,q)
        print(a)
        print(E1.mul(Coord(0,a),977))


check_identity(q,k)


def double_and_add(gl, g):
    """
    Returns the result of n * x, computed using
    the double and add algorithm.
    """
    for a in range(2,q-1):
        b=(a**2)%q
        if (4 * (a ** 3) + 27 * (b ** 2))  % q != 0:
            b=b=(a**2)%q
            a=a
            break
    result = Coord(0,0)
    addend = g
    if gl<=1023:
        i=10
    else:
        i=11
        E1 = EC(a,b , q)
        for[int(d) for d in bin(gl)[2:].zfill(8)][i] in [int(d) for d in bin(gl)[2:].zfill(8)]:
            if [int(d) for d in bin(gl)[2:].zfill(8)][i]== 1:
                result = E2.add(result,addend)
            addend =E2.add(addend,addend)
            i = i - 1
        return result



for gl in range(n1,n2+1):
    #print(n)
    double_and_add(gl, Coord(0, 2))
    if double_and_add(gl, Coord(0, 2))==(0,0):
           print(double_and_add(gl, Coord(0, 2)))
           print('ORDER İS:',gl)
    gl = gl + 1
    if gl==n2:
        print('there is no order in this interval for this n.')
        break
