#!/usr/bin/env python3

import sys


def largest_jolt(bank):
    j1 = max(bank[:-1])
    i1 = bank[:-1].index(j1)
    j2 = max(bank[i1+1:])
    return j1 * 10 + j2


def part1(lines):
    answer = 0
    for line in lines:
        bank = [int(a, 10) for a in line.strip()]
        jolt = largest_jolt(bank)
        answer += jolt
    return answer


def largest_jolt_12(bank):
    digits = []
    prev = -1
    N = len(bank)
    for i in range(12):
        bank_slice = bank[prev+1:N-(11-i)]
        j = max(bank_slice)
        digits.append(j)
        ji = bank_slice.index(j)
        prev = ji + prev + 1
    jolts = 0
    places = 1
    for j in reversed(digits):
        jolts += (places * j)
        places *= 10
    return jolts


def part2(lines):
    answer = 0
    for line in lines:
        bank = [int(a, 10) for a in line.strip()]
        jolt = largest_jolt_12(bank)
        answer += jolt
    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

