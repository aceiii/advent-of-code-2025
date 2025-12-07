#!/usr/bin/env python3

import sys
from math import prod
from itertools import zip_longest


def part1(lines):
    rows = [line.strip().split() for line in lines]
    last = rows.pop()
    rows = [list(map(int, row)) for row in rows]
    rows = zip(*rows)
    answer = 0
    for x, row in enumerate(rows):
        op = last[x]
        if op == '+':
            answer += sum(row)
        elif op == '*':
            answer += prod(row)
    return answer


def part2(lines):
    rows = [list(line) for line in lines]
    rows = zip_longest(*rows)
    op = None
    nums = []
    answer = 0
    for row in rows:
        row = list(row)
        while row and row[-1] is None:
            row.pop()
        if row[-1] in '+*':
            op = row.pop()

        num = ''.join(row).strip()
        if not num:
            total = sum(nums) if op == '+' else prod(nums)
            answer += total
            nums = []
            continue

        nums.append(int(num, 10))

    total = sum(nums) if op == '+' else prod(nums)
    answer += total
    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

