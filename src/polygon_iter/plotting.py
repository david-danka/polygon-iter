"""
Visualisation utilities for polygon sequences.
 
This module provides Matplotlib-based rendering of PolygonSequence objects.
Each polygon in the sequence is drawn as a separate line, allowing the full
iterative transformation to be visualised as an overlapping series of shapes.
"""

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
    """Render a PolygonSequence as an overlapping series of line plots.
 
    Each polygon is drawn as a single continuous line using its x and y
    coordinate lists. Axes are hidden and aspect ratio is locked to equal
    so the shapes are not distorted.
 
    Args:
        polygons: The sequence of polygons to render. Typically the output
            of iterate_polygon.
        figure_size: Width and height of the figure in inches, passed
            directly to Matplotlib as (width, height).
        color: Line colour for all polygons. Accepts any value supported
            by Matplotlib (named colours, hex strings, RGB tuples, etc.).
        alpha: Opacity of each line, in the range [0.0, 1.0]. Lower values
            allow overlapping polygons to show through each other, which
            is often visually effective for large iteration counts.
        show: Whether to display the figure interactively. Set to False
            when rendering headlessly or only saving to disk. Defaults to True.
        save_path: File path to save the figure. The format is inferred
            from the extension (e.g. '.png', '.svg', '.pdf'). If None,
            the figure is not saved. Defaults to None.
 
    Example:
        >>> polygon = Polygon.regular(6)
        >>> sequence = iterate_polygon(polygon, t=0.1, iterations=200)
        >>> plot_polygons(sequence, figure_size=(8, 8), color='indigo', alpha=0.15)
    """
    
    fig, ax = plt.subplots(figsize=figure_size)

    for polygon in polygons:
        ax.plot(
            polygon.x_coords(),
            polygon.y_coords(),
            color=color,
            alpha=alpha
        )

    ax.set_aspect('equal')
    ax.axis('off')

    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches='tight', pad_inches=0)
    if show:
        plt.show()
    
    plt.close(fig)