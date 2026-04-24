from dataclasses import dataclass
import math


@dataclass
class Point:
    x: float
    y: float

    def as_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)


@dataclass
class Polygon:
    points: list[Point]
    closed: bool = True

    def __len__(self):
        return len(self.points)
    
    def __iter__(self):
        return iter(self.points)
    
    def __getitem__(self, index: int) -> Point:
        return self.points[index]
    
    @classmethod
    def regular(
        cls,
        num_sides: int,
        radius: float = 1.0,
        center: Point = Point(0.0, 0.0),
        closed: bool = True
    ) -> "Polygon":
        
        """Create a regular polygon with the specified number of sides."""

        points = []
        if closed:
            num_points = num_sides + 1  # Include the first point to close the polygon
        else:
            num_points = num_sides
        
        central_angle = 2 * math.pi / num_sides

        # Rotate the polygon for a more visually appealing orientation
        if num_sides % 2 == 0:
            init_angle = central_angle / 2
        else:
            init_angle = central_angle / 2 - math.pi / 2
        
        for i in range(num_points):
            angle = init_angle + central_angle * i
            x = radius * math.cos(angle) + center.x
            y = radius * math.sin(angle) + center.y
            points.append(Point(x, y))

        return Polygon(points, closed)

    
    def x_coords(self) -> list[float]:
        return [p.x for p in self.points]
    
    def y_coords(self) -> list[float]:
        return [p.y for p in self.points]


@dataclass
class PolygonSequence:
    polygons: list[Polygon]
    t: float
    iterations: int

    def __len__(self):
        return len(self.polygons)

    def __iter__(self):
        return iter(self.polygons)