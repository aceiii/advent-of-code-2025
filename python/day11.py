#!/usr/bin/env python3

import sys
from math import prod
from collections import defaultdict


def parse_devices(lines):
    devices = defaultdict(lambda: set())
    for line in lines:
        name, rest = line.strip().split(':')
        devices[name] = set(rest.strip().split())
    return devices


def topsort(edges):
    arr = []
    s = []

    incoming = defaultdict(lambda: [])
    outgoing = defaultdict(lambda: [])
    nodes = set()
    for a, b in edges:
        incoming[b].append(a)
        outgoing[a].append(b)
        nodes.add(a)
        nodes.add(b)

    for n in nodes:
        if n not in incoming or not incoming[n]:
            s.append(n)

    while s:
        n = s.pop()
        arr.append(n)
        for n2 in outgoing[n]:
            incoming[n2].remove(n)
            if not incoming[n2]:
                s.append(n2)

    return arr


def get_edges(devices):
    edges = []
    for dev, out in devices.items():
        for dev2 in out:
            edges.append((dev, dev2))
    return edges


def count_paths(devices, start, end):
    sorted_dev = topsort(get_edges(devices))
    visits = defaultdict(lambda: 0)
    visits[start] = 1
    while sorted_dev:
        dev = sorted_dev.pop(0)
        n = visits[dev]
        for port in devices[dev]:
            visits[port] += n
    return visits[end]


def part1(lines):
    devices = parse_devices(lines)
    return count_paths(devices, 'you', 'out')


def part2(lines):
    devices = parse_devices(lines)
    a = [
        count_paths(devices, 'svr', 'dac'),
        count_paths(devices, 'dac', 'fft'),
        count_paths(devices, 'fft', 'out'),
    ]

    b = [
        count_paths(devices, 'svr', 'fft'),
        count_paths(devices, 'fft', 'dac'),
        count_paths(devices, 'dac', 'out'),
    ]
    return prod(a) + prod(b)


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

