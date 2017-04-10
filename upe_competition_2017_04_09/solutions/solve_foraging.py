#!/usr/bin/env python
import itertools
import math

timebudget = int(raw_input(), 10)

points = []
try:
    while True:
        tmp = raw_input()
        points.append([float(x) for x in tmp.split(' ')])
except EOFError:
    pass

def euclidean_distance(p1, p2):
    dx = (p2[0] - p1[0])**2
    dy = (p2[1] - p1[1])**2
    return math.sqrt(dx + dy)

def evaluate_cost(path):
    time = 0.0
    prev = [0, 0]
    path = list(path)
    path.append([0,0])
    for (i, point) in enumerate(path):
        time += (1 + i) * euclidean_distance(prev, point)
        prev = point
    return time

def prettyprint(path):
    bestpath = [[0,0]]
    bestpath.extend(path)
    bestpath.append([0,0])
    for point in bestpath:
        print('%.2f %.2f' % (point[0], point[1]))

    print '%.2f %d' % (evaluate_cost(bestpath[1:-1]), len(bestpath)-2)

def main():
    bestpaths = []
    bestfood = 0
    bestcost = float('inf')
    for i in range(len(points), 0, -1):
        for path in itertools.permutations(points, i):
            cost = evaluate_cost(path)
            if cost < timebudget and len(path) >= bestfood and cost <= bestcost:
                #print path, cost, bestcost
                if abs(cost - bestcost) < 0.0001:
                    bestpaths.append(path)
                elif cost < bestcost:
                    bestpaths = []
                    bestpaths.append(path)
                bestfood = len(path)
                bestcost = cost
    for path in bestpaths:
        prettyprint(path)
                    
main()
