#Construct a program that computes the number of elements in an elliptic curve group mod p.
#The program should make use of the following fact: An element a mod p has a square root if and only if
#a^(p-1)/2 eqv. to 1 mod p.
#Biz E(Zp) deki  noktaların sayı sını veren bir program kurmak istiyoruz.
#x in her değeri için f(x) in quadratic residue olduğu mod p de her durum bize 2 point verir, ve
#f(x)=0 değerini de veren 1 tane point var.
#Ama bunu quadratic residue sahip olan x leri, yani y^2=x mod p, bularak gösterebiliriz.Bunun için ,yani x in square
#root sahip olup olmadığını anlamak için: a^(p-1)/2 eqv. to 1 mod p. testini kullanıyoruz.



p=int(input('please enter a prime number p:'))
A=int(input('please enter  integer A which is in Zp:'))
B=int(input('please enter integer B which is in Zp:'))
def control_of_discriminant(A,B):
    d=4*A*A*A+27*B*B
    D=d%p
    print(D)
    if D==0:
        print('This cannot be an elliptic curve, please enter new A and B')
    else:
        print('Discriminant are satisfied.')



def AveBcontrol(A,B):
    if A>p and B>p:
        A=A%p
        B = B % p
    elif A<p and B>p:
        B=B%p
    elif A > p and B < p:
        A = A% p
    else:
        print('A and B values are ok.')


def f(x):
    k = x * x * x
    l = A * x
    m = B
    c=k+l+m
    return(c)

for x in range(0,p):
    AveBcontrol(A, B)

    print('f(',x,')=',f(x))
    a=f(x)%p
    print('f(',x,') on mod', p,' =',a)
    if a==0:
        print('one of the number of this elliptic curve is:',(x,a))
    s=(p-1)/2
    t=pow(a,s)
    Euler_criterion=t%p
    print('Euler_criterion=',Euler_criterion)
    if Euler_criterion==1:
        v=1
        v=2*v
        print(a,'is quadratic residue*********')
        print('Then we have two point in here!, we need to find y1 and y2.')
        for y in range(1, p):
            r = y * y
            g = r % p
            if g == a:
                print(y, 'is the y value')
                print('Then, the points are:',(x,y))

    x = x + 1


#we can call f(x) mod p as a.Then we need to compute a^(p-1)/2 is equal to 1 or not under mod p.
def number(x):
      v=1
      for x in range(0,p):
            print('f(',x,')=',f(x))
            a=f(x)%p
            print('f(',x,') on mod', p,' =',a)
            if a==0:
                print('one of the number of this elliptic curve is:',(x,a))
            s=(p-1)/2
            t=a**s
            Euler_criterion=t%p
            print('Euler_criterion=',Euler_criterion)
            if Euler_criterion==1:
                v=2*v
                print(a,'is quadratic residue*********')
                print('Then we have two point in here!, we need to find y1 and y2.')
      return(v)

print('CONCLUSION: Including the point at infinity, there are',number(x)+1,'elements in an elliptic curve group E(Zp).')

