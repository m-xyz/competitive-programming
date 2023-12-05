#! /usr/bin/env python
import argparse
from collections import defaultdict
from tqdm import tqdm

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")

ans = 0
cards = args['s'].read().splitlines()
N = len(cards)
d = defaultdict(int)

for idx, x in enumerate(cards):

    w_n, m_n = tuple(x[x.index(":")+1:].split("|"))
    w_n = w_n.split();m_n = m_n.split()
    d[idx] += 1
    matches = 0 

    for i in m_n:
        if(i in w_n):
            matches += 1

    if(matches): ans += (2 ** (matches - 1))

    for _ in range(d[idx]):
        for i in range(matches):
            if(idx + (i+1) < N):
                d[idx + (i+1)] += 1
    
print(f"Part 1: {ans}\nPart 2: {sum(d.values())}")
