#!/usr/bin/env python3

import sys
from collections import defaultdict


def parse_devices(lines):
    devices = defaultdict(lambda: set())
    for line in lines:
        name, rest = line.strip().split(':')
        devices[name] = set(rest.strip().split())
    return devices


def count_devices(ports, dev):
    print('dev',  dev)
    if dev == 'you':
        return 1
    return sum(count_devices(ports, d) for d in ports[dev])


def part1(lines):
    devices = parse_devices(lines)
    visits = defaultdict(lambda: 0)
    visits['you'] = 1
    q = ['you']
    while q:
        dev = q.pop(0)
        n = visits[dev]
        for port in devices[dev]:
            if port not in visits:
                q.append(port)
            visits[port] += n
            print('port', port, '=>',visits[port])
    return visits['out']


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

