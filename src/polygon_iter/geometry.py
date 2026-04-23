import math


def create_regular_polygon(
    num_sides: int,
    radius: float = 1.0,
    center: tuple[float, float] = (0.0, 0.0),
    closed: bool = True
)-> list[tuple[float, float]]:
    
    """Create a regular polygon with the specified number of sides."""

    points = []
    if closed:
        num_points = num_sides + 1  # Include the first point to close the polygon
    else:
        num_points = num_sides
    
    for i in range(num_points):
        angle = 2 * math.pi / num_sides * i
        x = radius * math.cos(angle) + center[0]
        y = radius * math.sin(angle) + center[1]
        points.append((x, y))
    return points


def transform_polygon(
    points: list[tuple[float, float]],
    t: float,
    closed: bool = True
) -> list[tuple[float, float]]:
    
    """Transform the polygon by moving each point towards the next point."""
    
    if closed:
        num_points = len(points) - 1  # Exclude the last point if it's the same as the first
    else:
        num_points = len(points)
    
    transformed_points = []
    for i in range(num_points + 1):
        x1, y1 = points[i % num_points]
        x2, y2 = points[(i + 1) % num_points]
        new_x = (1 - t) * x1 + t * x2
        new_y = (1 - t) * y1 + t * y2
        transformed_points.append((new_x, new_y))
    
    return transformed_points

def iterate_polygon(
    points: list[tuple[float, float]],
    t: float,
    iterations: int,
    closed: bool = True
) -> list[list[tuple[float, float]]]:
    
    """Iteratively transform the polygon for a specified number of iterations."""
    
    polygons = [points]
    for _ in range(iterations):
        new_points = transform_polygon(polygons[-1], t, closed)
        polygons.append(new_points)
    
    return polygons