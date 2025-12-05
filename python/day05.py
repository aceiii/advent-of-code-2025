#!/usr/bin/env python3

import sys


def range_overlaps(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return start2 >= start1 and start2 <= end1


def merge_range(range1, range2):
    rmin = min(range1[0], range2[0])
    rmax = max(range1[1], range2[1])
    return (rmin, rmax)


def merge_ranges(ranges):
    new_ranges = []
    ranges = ranges[:]
    while ranges:
        current_range = ranges.pop(0)
        while ranges and range_overlaps(current_range, ranges[0]):
            current_range = merge_range(current_range, ranges.pop(0))
        new_ranges.append(current_range)
    return new_ranges


def parse_ingredients(lines):
    mode = 0
    fresh_ids = []
    ingredient_ids = []
    for line in lines:
        line = line.strip()
        if not line:
            mode = 1
            continue
        if mode == 0:
            a, b = line.split('-')
            fresh_ids.append((int(a, 10), int(b, 10)))
        else:
            ingredient_ids.append(int(line, 10))
    fresh_ids = sorted(fresh_ids)
    return merge_ranges(fresh_ids), ingredient_ids


def find_closest_range(fresh_ranges, ingredient_id):
    for (start, end) in fresh_ranges:
        if end < ingredient_id:
            continue
        return (start, end)


def is_fresh(fresh_ranges, ingredient_id):
    fresh_range = find_closest_range(fresh_ranges, ingredient_id)
    if fresh_range is None:
        return False
    start, end = fresh_range
    return  ingredient_id >= start and ingredient_id <= end


def part1(lines):
    count = 0
    fresh_ids, ingredient_ids = parse_ingredients(lines)
    for ingredient_id in ingredient_ids:
        if is_fresh(fresh_ids, ingredient_id):
            count += 1
    return count


def part2(lines):
    answer = 0
    fresh_ids, _ = parse_ingredients(lines)
    for start, end in fresh_ids:
        answer += (end - start) + 1
    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

