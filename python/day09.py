#!/usr/bin/env python3

import sys
from operator import itemgetter


def parse_tiles(lines):
    tiles = []
    for line in lines:
        x, y = line.strip().split(',')
        tiles.append((int(x, 10), int(y, 10)))
    return tiles


def calc_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    return w * h


def part1(lines):
    tiles = sorted(parse_tiles(lines))
    answer = 0
    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i+1:]:
            area = calc_area(tile1, tile2)
            answer = max(answer, area)
    return answer


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

