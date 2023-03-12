#! /usr/bin/env python
def subarraysDivByK(A, K):
    res = 0
    prefix = 0
    count = [1] + [0] * K
    for a in A:
        print('current_prefix:',prefix)
        prefix = (prefix + a) % K
        res += count[prefix]
        count[prefix] += 1
        print('\tcount:', count[prefix])
    return res

subarraysDivByK([4,5,0,-2,-3,1], 5)

