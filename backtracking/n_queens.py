#!/usr/bin/env python

class NQueens:
    ans = 0

    def __init__(self, N):
        self.N = N

    def solve(self):
        print(self.N)
        
        col = set()
        d1 = set()
        d2 = set()

        def search(x):
            if(x == self.N):
                self.ans += 1
                return 

            for i in range(self.N):
                if(i in col or i + x in d1 or i - x in d2): continue

                col.add(i)
                d1.add(i + x)
                d2.add(i - x)

                search(x + 1)

                col.remove(i)
                d1.remove(i + x)
                d2.remove(i - x)

        search(0)

        return self.ans

N = int(input('Number of Queens:'))

nq = NQueens(N)

print("Number of ways you can place {NB} queens, in a {NB}x{NB} chessboard: {NQ}".format(NQ = nq.solve(), NB = N))

