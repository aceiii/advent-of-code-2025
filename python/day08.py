#!/usr/bin/env python3

import sys
from math import prod
from operator import itemgetter
from collections import defaultdict


def parse(lines):
    points = []
    for line in lines:
        x, y, z = line.strip().split(',')
        points.append((int(x, 10), int(y, 10), int(z, 10)))
    return points


def calc_dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx = x2-x1
    dy = y2-y1
    dz = z2-z1
    return dx*dx + dy*dy + dz*dz


def map_distances(points):
    dist = {}
    points = points[:]
    while points:
        p1 = points.pop()
        for p2 in points:
            d = calc_dist(p1, p2)
            dist[(p1,p2)] = d
    return dist


def union(connections, p1, p2):
    c1 = connections[p1]
    c2 = connections[p2]
    if c2 < c1:
        c1, c2 = c2, c1
    for p in connections:
        if connections[p] == c2:
            connections[p] = c1


def get_circuits(connections):
    circ_map = defaultdict(lambda: [])
    for point, cid in connections.items():
        circ_map[cid].append(point)
    return list(circ_map.values())


def part1(lines):
    N = 1000
    points = parse(lines)
    point_distances = map_distances(points)
    distances = sorted(point_distances.items(), key=itemgetter(1, 0))
    connections  = {p:i for i,p in enumerate(points)}
    for i in range(N):
        (p1, p2), _ = distances[i]
        union(connections, p1, p2)
    circuits = sorted(get_circuits(connections), key=lambda c: len(c), reverse=True)
    return prod(len(c) for c in circuits[:3])


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

