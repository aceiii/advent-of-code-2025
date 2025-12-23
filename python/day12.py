#!/usr/bin/env python3

import sys


def parse_shapes(lines):
    h = len(lines)
    w = len(lines[0])
    dims = (w, h)
    tiles = set()
    shapes = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                pos = x, y
                tiles.add(pos)
    return dims, tiles


def parse(lines):
    shapes = []
    shape = None
    regions = []

    for line in lines:
        line = line.strip()
        if line[-1:] == ':':
            shape = []
        elif line == '' and shape is not None:
            shapes.append(shape)
            shape = None
        elif 'x' in line:
            first, second = line.split(': ')
            dims = tuple(map(int, first.split('x')))
            counts = list(map(int, second.strip().split(' ')))
            regions.append((dims, counts))
        else:
            shape.append(line)
    return list(map(parse_shapes, shapes)), regions


def can_fit(region, shapes):
    (w, h), counts = region
    total_tiles = w * h
    num_tiles = 0
    for tm, ((tw, th), tiles) in zip(counts, shapes):
        tc = len(tiles)
        num_tiles += tm * tc
    return num_tiles <= total_tiles


def part1(lines):
    shapes, regions = parse(lines)
    answer = 0
    for region in regions:
        if can_fit(region, shapes):
            answer += 1
    return answer


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

