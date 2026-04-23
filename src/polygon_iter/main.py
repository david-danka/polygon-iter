from polygon_iter.geometry import create_regular_polygon, iterate_polygon
from polygon_iter.plotting import plot_polygons

def main():
    num_sides = 3
    polygon = create_regular_polygon(num_sides, closed=True)
    
    iterations = 2000
    transformation_ratio = 1/200

    polygons = iterate_polygon(
        polygon,
        t=transformation_ratio,
        iterations=iterations,
        closed=True
    )
    
    plot_polygons(polygons, figure_size=(8, 8), color='blue', alpha=0.1)

if __name__ == "__main__":
    main()