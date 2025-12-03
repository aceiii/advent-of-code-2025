#!/usr/bin/env python3

import sys
from math import ceil


def is_invalid(n):
    s = str(n)
    ln = len(s)
    if ln > 1 and ln % 2 == 0:
        if s[:ln//2] == s[ln//2:]:
            return True
    return False


def numlen(n):
    n = abs(n)
    ln = 0
    while n:
        n //= 10
        ln += 1
    return ln


def check_invalid_range(start, end):
    n = ceil(numlen(start)) / 2)
    m = ceil(numlenstr(end)) / 2)
    p = 10**n
    invalids = []
    #print(start//p, end // p + 1)
    for n in range(start // p, end // (10**m) + 1):
        if n >= p:
            p *= 10
        nn = n * p + n
        if nn >= start and nn <= end:
            invalids.append(nn)
    return invalids


def part1(lines):
    ranges = []
    for line in lines[0].strip().split(','):
        a, b = line.strip().split('-')
        ranges.append((int(a, 10), int(b, 10)))

    """
    answer = 0
    for (start, end) in ranges:
        for n in range(start, end+1):
            if is_invalid(n):
                answer += n
    """

    answer = 0
    for (start, end) in ranges:
        answer += sum(check_invalid_range(start, end))
    return answer


def is_invalid2(n):
    s = str(n)
    ln = len(s)
    if ln < 2:
        return False

    for i in range(1, ln):
        ss = s[:i]
        cnt = s.count(ss)
        if cnt == ceil(ln / i):
            return True

    return False


def part2(lines):
    ranges = []
    for line in lines[0].strip().split(','):
        a, b = line.strip().split('-')
        ranges.append((int(a, 10), int(b, 10)))

    answer = 0
    for (start, end) in ranges:
        for n in range(start, end+1):
            if is_invalid2(n):
                answer += n
    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

