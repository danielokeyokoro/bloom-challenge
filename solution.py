from typing import List
from collections import namedtuple
from functools import partial


Point = namedtuple("Point", "active x y z")


def distance(p1:Point, p2:Point):
    return (
          (p2.x - p1.x)**2
        + (p2.y - p1.y)**2
        + (p2.z - p1.z)**2
    ) ** 0.5


def transform(pointstr):
    d = pointstr.split(",")
    result = []

    for i, x in enumerate(d):
        if i == 0:
            result.append( int(x[1:]) )
        elif i == 3:
            result.append( int(x[:-1]) )
        else:
            result.append( int(x) )

    return result


def process_input(group:List[str]):
    return [ transform(point) for point in group ]


def pre_process(input_str):
    groups = input_str.split("\n")
    return [ process_input(group.split(";")) for group in groups ]


def greedy(acc, point, groups, route, lvl, memo):
    if not groups:
        return [acc, route]

    if (point, lvl) in memo:
        smallest, dist = memo.get( (point, lvl) )
    else:
        smallest = min([ Point(*p) for p in groups[0] if p[0] ], key=partial(distance, point))
        dist = distance(point, smallest)
        memo[(point, lvl)] = (smallest, dist)

    return greedy(acc+dist, smallest, groups[1:], route+[smallest], lvl+1, memo)


def shortestRoute(input_str):
    groups = pre_process(input_str)
    result = [float("inf"), []]

    memo = {}

    for p in groups[0]:
        if p[0]:
            candidate = greedy(0, Point(*p), groups[1:], [ Point(*p) ], 0, memo)
            if candidate[0] < result[0]:
                result = candidate

    return result


