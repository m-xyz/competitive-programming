#/usr/bin/env python
with open("day10_input.txt",'r') as f:

    CRT = ['.'] * 240
    sprite_pos = (0, 1, 2)
    cycles = 0
    val = 1
    CPU = {}
    for i in f:
        x = i.strip().split()
        if(x[0] == 'noop'):
            cycles += 1
            CPU[cycles] = (val,val)
        else:
            for i in range(2):
                cycles += 1
                CPU[cycles] = (val,val)
            old = val
            val += int(x[1])
            CPU[cycles] = (old, val)

ans = 0
cycles = 0
v = 20

while v <= 220:
    ans += CPU[v][0] * v
    v += 40
print("PART I:",ans,'\n')

for i in range(len(CRT)):
    cycles += 1
    xVal = CPU[cycles][0]
    sprite_pos = (xVal - 1, xVal, xVal + 1)
    if(i % 40 == sprite_pos[0] or i % 40 == sprite_pos[1] or i % 40 == sprite_pos[2]):
        CRT[i] = '#'
            
print("PART II:")
s = ""
for i in CRT:
    s += i
    if(len(s) == 40):
        print(s)
        s = ""
