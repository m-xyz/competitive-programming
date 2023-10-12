#! /usr/bin/env python

INT_MIN = -(2 ** 31)

def kadane(v):

    a, k = INT_MIN, 0

    for i in range(len(v)):

        k = max(v[i], k + v[i])
        a = max(a, k)

    return a 

in_v = input()
print('Max subarray of ',in_v,' :: ',kadane(eval(in_v)))
