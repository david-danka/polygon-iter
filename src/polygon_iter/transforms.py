from polygon_iter.primitives import Point, Polygon, PolygonSequence


def transform_polygon(
    polygon: Polygon,
    t: float
) -> Polygon:
    
    """Transform the polygon by moving each point towards the next point."""
    
    # Exclude the last point if it's the same as the first
    num_points = len(polygon) - 1 if polygon.closed else len(polygon)
    
    transformed_points = []
    for i in range(num_points + 1):
        p1 = polygon[i % num_points]
        p2 = polygon[(i + 1) % num_points]
        new_x = (1 - t) * p1.x + t * p2.x
        new_y = (1 - t) * p1.y + t * p2.y
        transformed_points.append(Point(new_x, new_y))
    
    return Polygon(transformed_points, polygon.closed)

def iterate_polygon(
    polygon: Polygon,
    t: float,
    iterations: int,
) -> PolygonSequence:
    
    """Iteratively transform the polygon for a specified number of iterations."""
    
    polygons = [polygon]
    for _ in range(iterations):
        polygons.append(transform_polygon(polygons[-1], t))
    
    return PolygonSequence(polygons, t, iterations)