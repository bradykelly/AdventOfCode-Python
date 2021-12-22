import copy
from grids.point import Point
class LineSegment: 

    def __init__(self, start: Point, end: Point) -> None:
        self.start = copy.deepcopy(start)
        self.end = copy.deepcopy(end)

    def __str__(self) -> str:
        return "Line from ({},{}) to ({},{})".format(self.start.y, self.start.x, self.end.y, self.end.x)    

    def length(self) -> int:
        return ((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** 0.5
