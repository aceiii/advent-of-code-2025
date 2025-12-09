#!/usr/bin/env python3

import sys
from math import prod
from operator import itemgetter
from collections import defaultdict
from itertools import groupby


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
    n = len(points)
    for i in range(n):
        p1 = points[i]
        for j in range(i+1, n):
            p2 = points[j]
            d = calc_dist(p1, p2)
            dist[(i, j)] = d
    return dist


def union(connections, reverse_connections, count, p1, p2):
    c1 = connections[p1]
    c2 = connections[p2]
    if c2 == c1:
        return count

    if c2 < c1:
        c1, c2 = c2, c1

    for i in reverse_connections[c2]:
        reverse_connections[c1].append(i)
        connections[i] = c1
    reverse_connections[c2] = []

    return count-1


def get_circuits(connections):
    circuits = []
    for key, group in groupby(sorted(connections)):
        items = list(group)
        circuits.append(items)
    return circuits


def part1(lines):
    N = 1000
    points = parse(lines)
    point_distances = map_distances(points)
    distances = sorted(point_distances.items(), key=itemgetter(1, 0))
    connections = list(range(len(points)))
    reverse_connections = {v:[v] for v in connections}
    count = len(connections)
    for (i, j), _ in distances[:N]:
        count = union(connections, reverse_connections, count, i, j)
    circuits = sorted(get_circuits(connections), key=lambda c: len(c), reverse=True)
    return prod(len(c) for c in circuits[:3])


def part2(lines):
    points = parse(lines)
    point_distances = map_distances(points)
    distances = sorted(point_distances.items(), key=itemgetter(1, 0))
    connections = list(range(len(points)))
    reverse_connections = {v:[v] for v in connections}
    count = len(connections)
    for (i, j), _ in distances:
        count = union(connections, reverse_connections, count, i, j)
        if count == 1:
            p1 = points[i]
            p2 = points[j]
            return p1[0] * p2[0]
            break


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

