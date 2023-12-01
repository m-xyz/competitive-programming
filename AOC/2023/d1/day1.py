#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-s", type=argparse.FileType('r'))
args = vars(parser.parse_args())
if(args['s'] == None): exit("No input file passed!\n")

def clean(s):
    d = {"one":"1", "two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}

    for k,v in d.items():
        s = s.replace(k, f"{k}{v}{k}")

    return s


v = args['s'].read().splitlines()
s = []

for i in range(len(v)):
    cv = clean(v[i])
    d = ""
    for j in range(len(cv)):
        if(cv[j].isdigit()): d += cv[j]
    s.append(int(d[0] + d[-1]))

print(sum(s))

