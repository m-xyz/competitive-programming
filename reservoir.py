#! /usr/bin/env python
import random

def selK(A, N, k = 1):

    i = 0

    reservoir = [0] * k

    for j in range(k):
        reservoir[j] = A[j]

    while(i < N):
        z = random.randrange(i + 1)

        if(z < k): reservoir[z] = A[i]

        i += 1

    print("Reservoir w/ %s samples: %s" % (len(reservoir), reservoir))


n = random.randint(1, 100)
a = [random.randrange(0,1000) for i in range(n)]
N = len(a)
k = int(input("k sample for reservoir: "))
if(k > N): k = N % k

selK(a, N, k)
