#! /usr/bin/env python3
import argparse
import numpy as np

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")

s = args['s'].read().splitlines()

def solve(p):

    ans = []

    if(p == 1): t, d = [list(map(int, i.split(":")[1].split())) for i in s]
    elif(p == 2): t, d = [list(map(int, ["".join(i.split(":")[1].split())])) for i in s]

    for i in range(len(t)):
        for j in range(t[i]):
            if(j * (t[i] - j) > d[i]):
                ans.append((t[i] - j) - j + 1)
                break

    return np.prod(ans)

print(f"Part 1: {solve(1)}\nPart 2: {solve(2)}")

