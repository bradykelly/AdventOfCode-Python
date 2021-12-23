import sys
import copy
from input_tool import InputTool
from grids.point import Point
from grids.line_segment import LineSegment

tool = InputTool()
origin = Point(0, 0)

def get_line_segments() -> list[LineSegment]:    
    input_lines = tool.input_lines_for_day(3, 2019)

    segments = []
    for line_no, input in enumerate(input_lines):
        directions  = tool.clean_split(input, ",")

        # Start each wire at the origin
        next_start = origin
        for dir in directions:

            # Before I follow any direction, the current segment's end point is the same as its start point
            this_line = LineSegment(next_start, next_start, line_no)

            delta = dir[0]
            length = int(dir[1:])

            if delta == "U":
                this_line.end.y += -length
            elif delta == "D":
                this_line.end.y += length
            elif delta == "L":
                this_line.end.x += -length
            elif delta == "R":
                this_line.end.x += length

            segments.append(copy.deepcopy(this_line))
            next_start = copy.deepcopy(this_line.end)

    return segments

def segments_cross_at(a: LineSegment, b: LineSegment) -> Point:
    ## If a and b are parallel, they won't cross
    #if (a.start.x == a.end.x and b.start.x == b.end.x) or (a.start.y == a.end.y and b.start.y == b.end.y):
    #    return None

    # If a is vertical and b is horizontal
    if (a.start.x == a.end.x) and (b.start.y == b.end.y):
        # And a is within b's range
        if (a.start.x >= b.start.x) and (a.start.x <= b.end.x):
            # And b is within a's range
            if (a.start.y >= b.start.y) and (a.start.y <= b.end.y):
                return Point(b.start.y, a.start.x)

    # If a is horizontal and b is vertical
    if (a.start.y == a.end.y) and (b.start.x == b.end.x):
        # And a is within b's range
        if (a.start.y >= b.start.y) and (a.start.y <= b.end.y):
            # And b is within a's range
            if (a.start.x >= b.start.x) and (a.start.x <= b.end.x):
                return Point(a.start.y, b.start.x)
    return None

def perpendicular_intersect_at(a, b) -> Point:
    if (a.line_no == b.line_no):
        return None
    if (a.start.x == a.end.x) and (b.start.y == b.end.y):
        # And a is within b's range
        if (a.start.x >= b.start.x) and (a.start.x <= b.end.x):
            # And b is within a's range
            if (a.start.y >= b.start.y) and (a.start.y <= b.end.y):
                return Point(b.start.y, a.start.x)

    return None

def all_segment_intersections() -> list[Point]:
    segs = get_line_segments()
    for segA in segs:
        for segB in segs:
            if segA.line_no == segB.line_no:
                continue
            intersectA = perpendicular_intersect_at(segA, segB)
            intersectB = perpendicular_intersect_at(segB, segA)
            if intersectA is not None:
                yield intersectA
            if intersectB is not None:
                yield intersectB

def manhattan_distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)

minDistance = sys.maxsize
for intersect in all_segment_intersections():
    if manhattan_distance(origin, intersect) < minDistance:
        minDistance = manhattan_distance(origin, intersect)

print(f"Part 1: {minDistance}")


