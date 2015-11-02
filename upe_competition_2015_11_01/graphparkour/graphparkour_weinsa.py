#!/usr/bin/env python
# UPE Programming competiton 2015-11-1 "graphparkour" solution by Avi Weinstock
import sys

def transpose(graph):
    result = dict()
    for (k,vs) in graph.items():
        for v in vs:
            result[v] = result.get(v,[])
            result[v].append(k)
    return result

def prune_by_heights(heights, edges):
    result = dict()
    for (k, vs) in edges.items():
        result[k] = result.get(k, [])
        for v in vs:
            if heights[v] < heights[k]:
                result[k].append(v)
    return result

def solver(heights, edges):
    # heights strictly decreasing -> cycles impossible
    # searching "longest path in a DAG" -> https://en.wikipedia.org/wiki/Longest_path_problem
    # sort-by-decreasing-height -> topological sort
    edges = prune_by_heights(heights, edges)
    backwards_edges = transpose(edges)
    vertices = sorted(heights.keys(), cmp=lambda u, v: heights[v]-heights[u]) # sort by largest-height-first
    paths = dict()
    for v in vertices:
        #print(v)
        acc = []
        for predecessor in backwards_edges.get(v,[]):
            #print(' '*4 + predecessor)
            tmp = paths.get(predecessor, [])
            if len(tmp) > len(acc):
                acc = list(tmp)
        acc.append(v)
        paths[v] = acc
    return sorted(paths.values(), key=lambda p: len(p))[-1]

def main():
    data = sys.stdin.read().split(';')[:-1]
    #print(data)
    heights = dict()
    edges = dict()
    for line in data:
        (vertex, rest) = line.split(':')
        (height, rest) = rest.split('-')
        dests = [x for x in rest.split(',') if len(x) > 0]
        heights[vertex] = int(height, 10)
        edges[vertex] = dests
    #print(heights)
    #print(edges)
    solution = solver(heights, edges)
    #print('->'.join(solution))
    print(len(solution))

if __name__ == '__main__':
    main()
