#!/usr/bin/env python3

import sys


def part1(lines):
    pos = 50
    answer = 0
    for line in lines:
        line = line.strip()
        direction, num = line[0], int(line[1:], 10)
        if direction == 'L':
            pos = (pos - num) % 100
        else:
            pos = (pos + num) % 100
        if pos == 0:
            answer += 1
    return answer


def part2(lines):
    pos = 50
    answer = 0
    for line in lines:
        line = line.strip()
        direction, num = line[0], int(line[1:], 10)

        to_zero = 100 if pos == 0 else (pos if direction == 'L' else 100 - pos)
        if num >= to_zero:
            answer += 1
            num -= to_zero
            pos = 0
        answer += num // 100
        if direction == 'L':
            pos = (pos - num) % 100
        else:
            pos = (pos + num) % 100

    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

