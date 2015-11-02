#!/usr/bin/env python
# UPE Programming competiton 2015-11-1 "trumptowers" solution by Avi Weinstock
import re
import sys

line_to_ints = lambda line: [int(x, 10) for x in re.split('  *', line)]

def bfs(graph, goal):
    queue = [1]
    steps = 0
    counter = 0
    while len(queue) > 0:
        steps += 1
        if steps > len(graph)**3:
            # Hack based on E <= V**2, so VE for finite BFS maxing out at V**3
            return 'INFINITE PATHS'
        current = queue.pop(0)
        nexts = graph.get(current, [])
        #print(current, nexts)
        for x in nexts:
            queue.append(x)
        if current == goal:
            counter += 1
    return str(counter)
            

def main():
    lines = sys.stdin.read().split('\n')
    (n, m) = line_to_ints(lines[0])
    #print(n,m)
    graph = dict()
    for line in lines[1:m+1]:
        (x,y) = line_to_ints(line)
        graph[x] = graph.get(x, [])
        graph[x].append(y)
    print(bfs(graph, n))

if __name__ == '__main__':
    main()

