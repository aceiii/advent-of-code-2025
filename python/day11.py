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


def count_paths(devices, start, end):
    visits = defaultdict(lambda: 0)
    visits[start] = 1
    q = [start]
    while q:
        dev = q.pop()
        #n = visits[dev]
        for port in devices[dev]:
            q.append(port)
            visits[port] += 1
    return visits[end]


def part1(lines):
    devices = parse_devices(lines)
    return count_paths(devices, 'you', 'out')


def reverse_devices(devices):
    rdevices = defaultdict(lambda: set())
    for dev, ports in devices.items():
        for port in ports:
            rdevices[port].add(dev)
    return rdevices


def count_parents(devices, start, end, cache=None):
    if end == start:
        return 1

    if cache is None:
        cache = {}
    if start in cache:
        return cache[start]

    count = sum(count_parents(devices, dev, end, cache) for dev in devices[start])
    cache[start] = count
    return count


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


def count_paths2(devices, start, end):
    graph = defaultdict(lambda: [])
    indegree = defaultdict(lambda: 0)

    edges = set()
    for dev, ports in devices.items():
        for port in ports:
            edges.add((dev, port))

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = []
    for i, n in indegree.items():
        if n == 0:
            q.append(i)

    top_order = []
    while q:
        node = q.pop(0)
        top_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    ways = defaultdict(lambda: 0)
    ways[start] = 1

    for node in top_order:
        for neighbor in graph[node]:
            ways[neighbor] += ways[node]

    return ways[end]


def get_edges(devices):
    edges = []
    for dev, out in devices.items():
        for dev2 in out:
            edges.append((dev, dev2))
    return edges


def count_paths3(devices, start, end):
    sorted_dev = topsort(get_edges(devices))
    visits = defaultdict(lambda: 0)
    visits[start] = 1
    while sorted_dev:
        dev = sorted_dev.pop(0)
        n = visits[dev]
        for port in devices[dev]:
            visits[port] += n
    return visits[end]


def part2(lines):
    devices = parse_devices(lines)
    a = [
        count_paths3(devices, 'svr', 'dac'),
        count_paths3(devices, 'dac', 'fft'),
        count_paths3(devices, 'fft', 'out'),
    ]

    b = [
        count_paths3(devices, 'svr', 'fft'),
        count_paths3(devices, 'fft', 'dac'),
        count_paths3(devices, 'dac', 'out'),
    ]
    return prod(a) + prod(b)


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

