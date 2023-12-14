#! /usr/bin/env python3
import argparse
import numpy as np
from collections import defaultdict
from functools import cmp_to_key

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")
cards_play = [(x.split()[0], int(x.split()[1])) for x in args['s'].read().splitlines()]

CARD_POWER = {"T": "A", "Q": "B", "K": "C", "A": "D", "J":"."}

def get_type(draw):

    if draw == "": return [""]

    r = []

    if(draw[0] == "J"): cards = "23456789TQKA"
    else: cards = draw[0]

    for c in cards:
        for t in get_type(draw[1:]):
            r.append(c + t)

    return r

def get_type2(hand):
        d = defaultdict(int)

        for cc in hand: d[cc] += 1

        c = sorted(d.values())
        
        match c:
            case [5]: return 6
            case [1,4]: return 5
            case [1,1,3]: return 3
            case [2,3]: return 4
            case [1,2,2]: return 2
            case [1,1,1,2]: return 1
            case _: return 0

def helper2(x): return max(map(get_type2, get_type(x)))

def helper(x): return (helper2(x), [CARD_POWER.get(c,c) for c in x])

ansp2 = 0

cards_play.sort(key=lambda y: helper(y[0]))

for idx, (_, bid) in enumerate(cards_play): ansp2 += (idx + 1) * bid

print(ansp2)

