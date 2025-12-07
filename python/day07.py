#!/usr/bin/env python3

import sys
from collections import defaultdict


def parse_diagram(lines):
    start = None
    splitters = set()
    for y, line in enumerate(lines):
        for x, tile in enumerate(line.strip()):
            pos = (x, y)
            if tile == 'S':
                start = pos
            elif tile == '^':
                splitters.add(pos)
    return start, splitters, y+1


def part1(lines):
    start, splitters, height = parse_diagram(lines)
    beams = set()
    beams.add(start)

    num_splits = 0
    while beams and any(b[1] < height for b in beams):
        new_beams = set()
        for bx, by in beams:
            by += 1
            if (bx, by) in splitters:
                new_beams.add((bx-1, by))
                new_beams.add((bx+1, by))
                num_splits += 1
            else:
                new_beams.add((bx, by))
        beams = new_beams
    return num_splits


def part2(lines):
    start, splitters, height = parse_diagram(lines)
    beams = set()
    beam_count = defaultdict(lambda: 0)

    beams.add(start)
    beam_count[start] = 1

    while beams and any(b[1] < height for b in beams):
        new_beams = set()
        for beam in beams:
            bx, by = beam
            count = beam_count[beam]
            by += 1
            new_beam = (bx, by)
            left_beam = (bx-1, by)
            right_beam = (bx+1, by)
            if new_beam in splitters:
                new_beams.add(left_beam)
                new_beams.add(right_beam)
                beam_count[left_beam] += count
                beam_count[right_beam] += count
            else:
                new_beams.add(new_beam)
                beam_count[new_beam] += count
        beams = new_beams

    answer = 0
    for beam in beams:
        answer += beam_count[beam]
    return answer



def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

