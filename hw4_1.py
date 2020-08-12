#construct a program whose inputs are integers a,b,p and output is a^b  mod p.
#the program should have at most 3logp mod p.


import math
a = int(input("Enter an integer as 'a' : "))
b = int(input("Enter an integer as 'b' : "))
p = int(input("Enter an prime number as 'p' bigger than a and b : "))
sum_result=[]
count = []
result = 1

def find_binary(b):
    binary = []
    count1 = 0
    q= 1
    while (b>= 2):
        q = b//2
        r=b%2 binary.append(r)
        b= q
    count1 = count1 +1
    binary.append(q)
    print("binary is {}".format(binary)) return binary, count1


def power(x,j,root): count2 = 0
    for i in range (x-j):
        root = (root * root)%p
        count2 = count2 +1
    print("mul is {}".format(root))
    return root, count2


if (b == p-1):
    result = 1
else:
while (b>=p):
    b = b-(p-1)
    result_binary, count_binary = find_binary(b)
    count.append(count_binary)
    j= 0
    for i in range(len(result_binary)):
        result_mult = []
        count_pow = []
    if result_binary[i] == 1:
    if j == 0:
        result_mult, count_pow = power(i,0,a)
    else:
        result_mult, count_pow = power(i,j,sum_result[-1])
sum_result.append(result_mult) j= i
count.append(count_pow)
print("sum result = {}".format(sum_result))



count3 = 0
for i in range(len(sum_result)):
    result = (result * sum_result[i])%p
    count3 = count3 +1
    count.append(count3)



print("result is {}".format(result))
performans = sum(count)
number = 3*(math.log(p)/math.log(2))
print("performans = {} and 3 log p {}".format(performans, number))
