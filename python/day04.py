#!/usr/bin/env python3

import sys


def get_dimensions(rows):
    height = len(rows)
    width = len(rows[0])
    return (width, height)


def neighbours(pos):
    x, y = pos
    yield (x, y-1)
    yield (x+1, y-1)
    yield (x+1, y)
    yield (x+1, y+1)
    yield (x, y+1)
    yield (x-1, y+1)
    yield (x-1, y)
    yield (x-1, y-1)


def traverse(dims):
    width, height = dims
    for y in range(height):
        for x in range(width):
            yield (x, y)


def within_bounds(dims, pos):
    width, height = dims
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


def count_adjacent_rolls(rows, dims, pos):
    count = 0
    for npos in neighbours(pos):
        if not within_bounds(dims, npos):
            continue
        nx, ny = npos
        ntile = rows[ny][nx]
        if ntile == '@':
            count += 1
    return count


def print_map(rows, tile_func=lambda tile, pos: tile):
    for y, row in enumerate(rows):
        for x, tile in enumerate(row):
            pos = (x, y)
            print(tile_func(tile, pos), end='')
        print('')


def part1(lines):
    valid_rolls = set()
    dims = get_dimensions(lines)
    for pos in traverse(dims):
        x, y = pos
        tile = lines[y][x]
        if tile != '@':
            continue
        if count_adjacent_rolls(lines, dims, pos) < 4:
            valid_rolls.add(pos)
    #print_map(lines, lambda tile, pos: 'X' if pos in valid_rolls else tile)
    return len(valid_rolls)


def removable_rolls(rows):
    valid_rolls = set()
    dims = get_dimensions(rows)
    for pos in traverse(dims):
        x, y = pos
        tile = rows[y][x]
        if tile != '@':
            continue
        if count_adjacent_rolls(rows, dims, pos) < 4:
            valid_rolls.add(pos)
    return valid_rolls


def remove_rolls(rows, to_remove):
    new_rows = []
    for y, row in enumerate(rows):
        new_row = []
        for x, tile in enumerate(row):
            pos = x, y
            if pos in to_remove:
                new_row.append('.')
            else:
                new_row.append(tile)
        new_rows.append(''.join(new_row))
    return new_rows


def part2(lines):
    rows = lines
    removed = 0
    to_remove = removable_rolls(rows)
    while to_remove:
        removed += len(to_remove)
        rows = remove_rolls(rows, to_remove)
        to_remove = removable_rolls(rows)
    return removed

def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

