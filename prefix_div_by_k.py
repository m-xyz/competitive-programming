#! /usr/bin/env python
def subarraysDivByK(A, K):
    res = 0
    prefix = 0
    count = [1] + [0] * K
    for a in A:
        prefix = (prefix + a) % K
        res += count[prefix]
        count[prefix] += 1
    return res
A = [4,5,0,-2,-3,1]
k = 5
r = subarraysDivByK(A, k)
print('\tNumber of subarrays in',A,'divisable by',k,':', r)

