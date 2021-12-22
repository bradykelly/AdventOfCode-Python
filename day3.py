from input_tool import InputTool
from grids.point import Point
from grids.line_segment import LineSegment

tool = InputTool()
input_lines = tool.input_lines_for_day(3, 2019)

origin = Point(0, 0)
next = origin

segments = []
for line in input_lines:

    directions  = tool.clean_split(line, ",")

    for dir in directions:

        this_line = LineSegment(start=next, end=next)

        delta = dir[0]
        length = int(dir[1:])

        if delta == "U":
            this_line.end.y = -length
        elif delta == "D":
            this_line.end.y = length
        elif delta == "L":
            this_line.end.x = -length
        elif delta == "R":
            this_line.end.x = length

        segments.append(this_line)
        next = this_line.end
