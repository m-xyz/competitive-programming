#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")

BOUNDS = {"red":12, "green":13, "blue":14}
MIN_VALS = {"red":0, "green":0, "blue":0}
ans1 = 0; ans2 = 0

for idx, i in enumerate(args['s'].read().splitlines()):
    gg = True
    for j in i.split(':')[1].strip().split(';'):
        for k in j.split(','):
            k = tuple(k.strip().split(' '))
            if(MIN_VALS[k[1]] < int(k[0])): MIN_VALS[k[1]] = int(k[0])
            if(BOUNDS[k[1]] < int(k[0])): gg = False
    if(gg): ans1 += idx+1
    ans2 += (MIN_VALS["red"]*MIN_VALS["green"]*MIN_VALS["blue"])
    MIN_VALS["red"] = 0;MIN_VALS["green"] = 0;MIN_VALS["blue"] = 0

print(f"Part 1: {ans1}\nPart 2:{ans2}\n")
