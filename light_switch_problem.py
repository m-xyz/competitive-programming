#! /usr/bin/env python

#led = [[0] * 10 for _ in range(10)]
led = [False] * 100

step = 1

while step <= 100:

    for i in range(0,len(led), step):
        led[i] = not led[i]

    step += 1

for i in range(len(led)):
    if(led[i]):
        print('Lightbulb @',i,'ON')

