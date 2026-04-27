"""
Command-line interface for the polygon iteration visualiser.
 
Exposes the full pipeline — polygon construction, iterative transformation,
and rendering — as a single command with configurable parameters.
 
Typical usage:
    $ python -m polygon_iter --num-sides 6 --iterations 500 --t 0.2 --color indigo --alpha 0.1
    $ python -m polygon_iter --num-sides 3 --save-path output.png --no-show
"""

import argparse
from polygon_iter.primitives import Polygon
from polygon_iter.transforms import iterate_polygon
from polygon_iter.plotting import plot_polygons


def build_parser() -> argparse.ArgumentParser:
    """Construct and return the argument parser.
 
    Separated from main() so the parser can be reused in tests
    without triggering the full pipeline.
 
    Returns:
        A configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="polygon-iter",
        description="Visualise iterative linear interpolation on regular polygons.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
 
    parser.add_argument(
        "-n", "--num-sides",
        type=int,
        default=5,
        metavar="SIDES",
        help="Number of sides of the base polygon. Must be >= 3.",
    )
    parser.add_argument(
        "-i", "--iterations",
        type=int,
        default=200,
        metavar="STEPS",
        help="Number of transformation steps to apply.",
    )
    parser.add_argument(
        "-r", "--ratio",
        type=float,
        default=0.2,
        metavar="RATIO",
        help=(
            "Interpolation ratio applied at each step."
        ),
    )
    parser.add_argument(
        "-c", "--color",
        type=str,
        default="blue",
        metavar="COLOR",
        help="Line colour. Accepts any Matplotlib colour string (e.g. 'red', '#ff0000').",
    )
    parser.add_argument(
        "-a", "--alpha",
        type=float,
        default=1.0,
        metavar="OPACITY",
        help="Line opacity in the range [0.0, 1.0]. Lower values suit large iteration counts.",
    )
    parser.add_argument(
        "--figure-size",
        type=int,
        nargs=2,
        default=[8, 8],
        metavar=("WIDTH", "HEIGHT"),
        help="Figure dimensions in inches.",
    )
    parser.add_argument(
        "--save-path",
        type=str,
        default=None,
        metavar="PATH",
        help="File path to save the figure (e.g. output.png). Format inferred from extension.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Suppress the interactive plot window. Useful when only saving to disk.",
    )
 
    return parser

def cli() -> None:
    """Parse arguments and run the polygon iteration pipeline."""
    parser = build_parser()
    args = parser.parse_args()
 
    if args.num_sides < 3:
        parser.error("--num-sides must be >= 3.")
 
    polygon = Polygon.regular(args.num_sides, closed=True)
 
    polygons = iterate_polygon(
        polygon,
        t=args.ratio,
        iterations=args.iterations,
    )

    plot_polygons(
        polygons,
        figure_size=tuple(args.figure_size),
        color=args.color,
        alpha=args.alpha,
        show=not args.no_show,
        save_path=args.save_path,
    )