"""
Entry point for the polygon iteration visualiser.
 
Demonstrates the full pipeline: constructing a regular polygon, applying
an iterative linear interpolation transform, and rendering the resulting
sequence as a layered plot.
 
Typical invocation:
    $ python -m polygon_iter
"""

from polygon_iter.primitives import Polygon
from polygon_iter.transforms import iterate_polygon
from polygon_iter.plotting import plot_polygons


def main():
    """Run the polygon iteration pipeline with default parameters.
 
    Constructs a regular polygon, iteratively transforms it, and plots
    the full sequence. Tweak num_sides, iterations, and transformation_ratio
    to explore different visual outcomes.
 
    Notable behaviours:
        - Positive t rotates the spiral inward in one direction.
        - Negative t produces an outward or counter-rotating spiral.
        - Large iteration counts with small t values yield smooth spirals.
    """
    num_sides = 4
    polygon = Polygon.regular(num_sides, closed=True)
    
    iterations = 3
    transformation_ratio = -1/3

    polygons = iterate_polygon(
        polygon,
        t=transformation_ratio,
        iterations=iterations
    )
    
    plot_polygons(polygons, figure_size=(8, 8), color='blue', alpha=1)

if __name__ == "__main__":
    main()