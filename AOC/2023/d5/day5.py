#! /usr/bin/env python3
import argparse
import sys
from collections import defaultdict

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")

x = args['s'].read().splitlines()
N = len(x)
seeds = list(map(lambda x: int(x),x[0].split(' ')[1:]))
ff = []; tmp = []

for i in range(N):
    if(x[i] == ''):
        if(tmp):
            ff.append(tmp)
            tmp = []
    elif(x[i][0].isdigit()):
        t = tuple(map(lambda x: int(x),x[i].split(' ')))
        tmp.append(t)
if(tmp): ff.append(tmp)

def get_location(seeds):

    location = []
    best_min = sys.maxsize
    for seed in seeds:
        curr_seed = seed
        for i in range(7):
            tmp_seed = curr_seed
            for j in ff[i]:
                if(curr_seed <= (j[2] + j[1]) and curr_seed >= j[1]):
                    tmp_seed = (curr_seed - j[1]) + j[0]
                    break
            curr_seed = tmp_seed
        best_min = min(best_min, curr_seed)
        location.append(curr_seed)
    location.sort()
    return location

print(f"Part 1: {get_location(seeds)[0]}\n")
