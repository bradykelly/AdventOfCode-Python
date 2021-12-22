import copy
from input_tool import InputTool
from grids.point import Point
from grids.line_segment import LineSegment

tool = InputTool()
input_lines = tool.input_lines_for_day(3, 2019)

origin = Point(0, 0)

segments = []
for line in input_lines:
    directions  = tool.clean_split(line, ",")

    # Start each wire at the origin
    next_start = origin
    for dir in directions:

        # Before I follow any direction, the current segment's end point is the same as its start point
        this_line = LineSegment(start=next_start, end=next_start)

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
