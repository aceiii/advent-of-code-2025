#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict

DIR_MAP = [(0,1), (-1, 0), (0, -1), (1, 0)]


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


def get_dir(edge):
    (ax, ay), (bx, by) = edge
    dx = bx - ax
    dy = by - ay
    if dy > 0:
        return 0
    elif dx < 0:
        return 1
    elif dy < 0:
        return 2
    else:
        return 3


def dir_sign(ax, bx):
    dx = bx - ax
    if dx == 0:
        return 0
    return -1 if dx < 0 else 1


def tiles_between(edge):
    (ax, ay), (bx, by) = edge
    if is_vert(edge):
        dy = by - ay
        d = -1 if dy < 0 else 1
        x = ax
        y = ax
        for i in range(abs(dy)+1):
            y += d
            yield (x, y)
    else:
        pass


def edge_intersects(vert_edge, horz_edge, debug=False):
    (ax, ay), (bx, by) = vert_edge
    (cx, cy), (dx, dy) = horz_edge

    x = ax
    y = cy
    top = min(ay, by)
    bottom = max(ay, by)
    left = min(cx, dx)
    right = max(cx, dx)

    if debug:
        print('edge_intersects', vert_edge, horz_edge, x, y, left, right, top, bottom, x >= left and x <= right and y >= top and y <= bottom)

    return x >= left and x <= right and y >= top and y <= bottom


def crosses_edges(edges, edge, debug=False):
    vert, horz = edges
    if is_vert(edge):
        for edge2 in horz:
            if edge_intersects(edge, edge2, debug):
                return True
    else:
        for edge2 in vert:
            if edge_intersects(edge2, edge, debug):
                return True
    return False


def is_vert(edge):
    (ax, ay), (bx, by) = edge
    dx = bx - ax
    dy = by - ay
    return dx == 0


def group_edges(edges):
    vert = []
    horz = []
    for edge in edges:
        if is_vert(edge):
            vert.append(edge)
        else:
            horz.append(edge)

    sorted_vert = sorted(vert, key=lambda x:(x[0][0], min(x[0][1], x[1][1]), max(x[0][1], x[1][1])))
    sorted_horz = sorted(horz, key=lambda x:(min(x[0][0], x[1][0]), max(x[0][0], x[1][0]), x[0][1]))
    return sorted_vert, sorted_horz


def expand_edges(edges):
    outline = []
    for idx, edge in enumerate(edges):
        next_edge = edges[(idx + 1) % len(edges)]
        prev_edge = edges[(idx - 1) % len(edges)]

        edge_dir = get_dir(edge)
        next_edge_dir = get_dir(next_edge)
        prev_edge_dir = get_dir(prev_edge)

        (dx, dy) = DIR_MAP[(edge_dir - 1) % len(DIR_MAP)]
        (ax, ay), (bx, by) = edge
        (vx, vy), (wx, wy) = (ax + dx, ay + dy), (bx + dx, by + dy)

        if prev_edge_dir == (edge_dir + 1) % len(DIR_MAP):
            if edge_dir == 0:
                vy += 1
            elif edge_dir == 1:
                vx -= 1
            elif edge_dir == 2:
                vy -= 1
            else:
                vx += 1
        else:
            if edge_dir == 0:
                vy -= 1
            elif edge_dir == 1:
                vx += 1
            elif edge_dir == 2:
                vy += 1
            else:
                vx -= 1

        if next_edge_dir == (edge_dir - 1) % len(DIR_MAP):
            if edge_dir == 0:
                wy -= 1
            elif edge_dir == 1:
                wx += 1
            elif edge_dir == 2:
                wy += 1
            else:
                wx -= 1
        else:
            if edge_dir == 0:
                wy += 1
            elif edge_dir == 1:
                wx -= 1
            elif edge_dir == 2:
                wy -= 1
            else:
                wx += 1

        outline.append(((vx, vy), (wx, wy)))
    return outline


def calc_outside_edges(tile1, tile2):
    ax, ay = tile1
    bx, by = tile2

    top = min(ay, by)
    bottom = max(ay, by)
    left = min(ax, bx)
    right = max(ax, bx)

    top_vert_edge = ((left, top), (right, top))
    bottom_vert_edge = ((left, bottom), (right, bottom))
    left_horz_edge = ((left, top), (left, bottom))
    right_horz_edge = ((right, top), (right, bottom))

    return (top_vert_edge, bottom_vert_edge, left_horz_edge, right_horz_edge)


def part2(lines):
    tiles = parse_tiles(lines)
    edges = list(zip(tiles, tiles[1:] + tiles[:1]))
    vert, horz = group_edges(edges)

    outline = expand_edges(edges)

    sorted_areas = []
    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i+1:]:
            area = calc_area(tile1, tile2)
            sorted_areas.append((area, calc_outside_edges(tile1, tile2)))

    sorted_areas.sort(reverse=True)
    outline_edges = group_edges(outline)
    for area, edges in sorted_areas:
        if all(not crosses_edges(outline_edges, edge) for edge in edges):
            return area


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

