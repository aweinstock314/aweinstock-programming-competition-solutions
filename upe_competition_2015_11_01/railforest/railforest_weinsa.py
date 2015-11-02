#!/usr/bin/env python
# UPE Programming competiton 2015-11-1 "railforest" solution by Avi Weinstock
import re
import sys

INFINITY = float('inf')
line_to_ints = lambda line: [int(x, 10) for x in re.split('  *', line)]

def solver(width, height, grid):
    prevs = [[0, list()] for _ in range(width)]
    for (y, line) in enumerate(grid):
        #print(line)
        currents = []
        for (x,cost) in enumerate(line):
            if cost < 0:
                cost = INFINITY
            cur = [INFINITY, []]
            for dx in [-1,0,1]:
                if x+dx < 0 or x+dx >= width:
                    continue
                #print(x,x+dx)
                tmp = prevs[x+dx]
                if tmp[0]+cost < cur[0]:
                    cur[0] = tmp[0] + cost
                    cur[1] = tmp[1] + [x]
            currents.append(cur)
        prevs = currents
    solution = min([x for (x,_) in prevs])
    if solution == INFINITY:
        solution = -1
    return solution

def main():
    lines = sys.stdin.read().split('\n')
    (height, width) = line_to_ints(lines[0])
    #print(height,width)
    grid = [line_to_ints(line) for line in lines[1:height+1]]
    print(solver(width, height, grid))

if __name__ == '__main__':
    main()
