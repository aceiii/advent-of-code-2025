#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import product


def parse_line(line):
    lights = []
    buttons = []
    joltages = []
    for part in line.strip().split(' '):
        brace, inner = part[0], part[1:-1]
        if brace == '[':
            lights = [0 if a == '.' else 1 for a in inner]
        else:
            item = list(map(lambda a: int(a, 10), inner.split(',')))
            if  brace == '(':
                buttons.append(set(item))
            elif brace == '{':
                joltages.append(item)
    return lights, buttons, joltages


def format_masks(row):
    target = 0
    masks = []
    light, buttons, _ = row
    for c in light:
        target <<= 1
        target |= c
    n = len(light)
    for btn in buttons:
        mask = 0
        for b in btn:
            mask ^= 1<<(n-b-1)
        masks.append(mask)
    return target, masks


def parse(lines):
    return [format_masks(parse_line(line)) for line in lines]


def solve(target, buttons, debug=False):
    N = len(buttons)
    q = [(0, 0, 0) for i in range(N)]
    while q:
        current, i, n = q.pop(0)
        nn = n+1
        for j in range(i,N):
            btn = buttons[j]
            new = current ^ btn
            if new == target:
                return nn
            q.append((new, j+1,  nn))


def part1(lines):
    row = parse(lines)
    answer = 0
    for i, (lights, buttons) in enumerate(row):
        answer += solve(lights, buttons, debug=i==88)
    return answer


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

