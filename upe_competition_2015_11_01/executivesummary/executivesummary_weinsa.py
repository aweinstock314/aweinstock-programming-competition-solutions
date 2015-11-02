#!/usr/bin/env python
# UPE Programming competiton 2015-11-1 "executivesummary" solution by Avi Weinstock
import sys
import re

line_to_floats = lambda line: [float(x) for x in re.split('  *', line)]

def main():
    lines = sys.stdin.read().split('\n')
    (radius,) = line_to_floats(lines[0])
    #print(radius)
    ts = []
    rs = []
    for line in lines[1:]:
        data = re.split('  *', re.sub(',', '', line))
        if len(data) != 3:
            continue
        (ty, x, y) = data
        (x, y) = map(float, (x,y))
        if ty == 'T':
            ts.append((x,y))
        elif ty == 'R':
            rs.append((x,y))
        else:
            assert False, "Found an item that's neither a transmitter nor receiver"

    successes = 0
    for (x,y) in rs:
        for (a,b) in ts:
            sqrdist = ((a-x)**2 + (b-y)**2)
            #print((x,y),(a,b),sqrdist)
            if sqrdist < radius**2:
                successes += 1
                break
    ratio = successes / float(len(rs))
    print("%0.2f" % (ratio*100,))

if __name__ == '__main__':
    main()
