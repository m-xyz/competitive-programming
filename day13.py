#!/usr/bin/env python
with open("day13_input.txt",'r') as f:

    part = int(input('PART(1/2):'))

    def solve(x:list,y:list):

        if(isinstance(x,int) and isinstance(y,int)):

            if(x > y):
                return -1
            if(x < y):
                return 1
            elif(x == y):
                return 0

        elif(isinstance(x,list) and isinstance(y,list)):

            i = 0
            while i < len(x) and i < len(y):
                r = solve(x[i], y[i])

                if r == -1:
                    return -1
                if r == 1:
                    return 1

                i += 1

            if(i == len(x) and i < len(y)):
                return 1
            elif(i == len(y) and i < len(x)):
                return -1
        elif(isinstance(x,list) and isinstance(y,int)):
            return solve(x, [y])
        else:
            return solve([x],y)

    v = []

    for i in f:
        try:
            v.append(eval(i.strip()))
        except:
            pass

    if(part == 2):

        v.append([[2]])
        v.append([[6]])
        k = 1
        done = 0

        while True:
            r = solve(v[k-1],v[k])
            if(r != 1):
                t = v[k-1]
                v[k-1] = v[k]
                v[k] = t
                done = 0
            elif(r == 1):
                done += 1
                if(done == len(v)):
                    break
            k+=1
            if(k >= len(v)):
                k = 1
        t = 0
        s = 0

        for i in range(len(v)):
            if(v[i] == [[2]]):
                t = i + 1

            if(v[i] == [[6]]):
                s = i + 1
        print(f'PART_2: {t*s}')
    else:
        idx = [-1] * (len(v) // 2)
        i = 0
        for k in range(1,len(v), 2):
           idx[i] = solve(v[k-1],v[k])
           i += 1

        ans = 0
        for i in range(len(idx)):
            if(idx[i] == 1):
                ans += (i + 1)
        print(f'PART_1: {ans}')
