import copy
from grids.point import Point
class LineSegment: 

    def __init__(self, start: Point, end: Point, line_no: int) -> None:
        self.start = copy.deepcopy(start)
        self.end = copy.deepcopy(end)
        self.line_no = line_no

    def __str__(self) -> str:
        return f"Line from ({self.start.y}, {self.start.x}) to ({self.end.y}, {self.end.x})"

    def length(self) -> int:
        return ((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** 0.5
