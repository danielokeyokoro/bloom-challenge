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


def brute(acc, point, groups, route, total):
    if not groups:
        total.append( [acc, route] )
        return

    points = [ Point(*po) for po in groups[0] if po[0] ]

    for p in points:
        dist = distance(point, p)
        brute(acc+dist, p, groups[1:], route+[p], total)


def shortestRoute(input_str):
    groups = pre_process(input_str)

    total = []

    for p in groups[0]:
        if p[0]:
            brute(0, Point(*p), groups[1:], [ Point(*p) ], total)

    return min(total, key=lambda x: x[0])


