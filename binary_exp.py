#! /usr/bin/env python
from datetime import datetime
#Recursive
def bin_exp(k, b):
    if(b == 0):
        return 1
    x = bin_exp(k, b // 2)
    if(b % 2 == 1):
        return x * x * k
    return x * x

#Iterative
def bin_exp_it(k, b):
    r = 1
    while(b > 0):
        if(b % 2 == 1): r *= k
        k *= k
        b //= 2

    return r

print(bin_exp_it(2, 3))

#t0 = datetime.now()
#z = bin_exp(13332,58)
#t1 = datetime.now()
#
#print('bin_exp',z, t1-t0)
#
#t2 = datetime.now()
#dz = 13332 ** 58
#t3 = datetime.now()
#
#print('normal',dz, t3-t2)

