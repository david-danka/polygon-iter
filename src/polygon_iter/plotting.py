import matplotlib.pyplot as plt
from polygon_iter.primitives import PolygonSequence

def plot_polygons(
    polygons: PolygonSequence,
    figure_size: tuple[int, int],
    color: str,
    alpha: float,
    show: bool = True,
    save_path: str | None = None,
) -> None:
    
    """Plot the list of polygons using Matplotlib."""
    
    plt.figure(figsize=figure_size)

    for polygon in polygons:
        plt.plot(
            polygon.x_coords(),
            polygon.y_coords(),
            color=color,
            alpha=alpha
        )

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    if show:
        plt.show()
    
    plt.close()