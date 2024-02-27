"""Provides helper functions and classes related to geometries.
"""

# Standard library imports
from decimal import Context, Decimal, ROUND_HALF_UP
from typing import List

# Third-party imports
from shapely import box, Polygon


class BoundingBox:
    """Simple data struture for a bounding box based on EPSG:4326 coordinates."""

    def __init__(self, min_x: float, max_x: float, min_y: float, max_y: float) -> None:
        """Initializes a new instance of a `BoundingBox`.

        Args:
            min_x (`Decimal`): The minimum longitude (i.e., x-coordinate).

            max_x (`Decimal`): The maximum longitude (i.e., x-coordinate).

            min_y (`Decimal`): The minimum latitude (i.e., y-coordinate).

            max_y (`Decimal`): The maximum latitude (i.e., y-coordinate).

        Returns:
            `None`
        """
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    @property
    def width(self) -> Decimal:
        """The width of the box in degrees."""
        return self.max_x - self.min_x

    @property
    def height(self) -> Decimal:
        """The width of the box in degrees."""
        return self.max_y - self.min_y

    def split_along_axes(self, x_into: int, y_into: int) -> List["BoundingBox"]:
        """Splits the bounding box into a given number of units in
        the x- and y-directions to create a list of smaller bounding boxes.
        For example, the arguments `x_into=2` and `y_into=3` would
        divide the bounding box into two pieces along the x-axis and
        three pieces along the y-axis, for a total of six smaller boxes,
        each of which would be half of the original width and one-third of
        the original height.

        Raises:
            `ValueError` if `x_into` or `y_into` is less than or equal to zero.

        Args:
            x_into (`int`): The number of pieces the bounding box should
                be split into along the x-axis.

            y_into (`int`): The number of pieces the bounding box should
                be split into along the y-axis.

        Returns:
            (`list` of `BoundingBox`): The bounding boxes.
        """
        # Validate arguments
        if (x_into <= 0) or (y_into <= 0):
            raise ValueError(
                "Unable to split bounding box. Expected the number of slices "
                "to make along the x- and y-axes to be positive numbers."
            )

        # Initialize rounding strategy to prevent long decimals
        context = Context(rounding=ROUND_HALF_UP)

        # Define dimensions of bounding box "slices"
        slice_width = self.width / x_into
        slice_height = self.height / y_into

        # Subdivide bounding box into slices
        slices = []
        for i in range(x_into):
            slice_min_x = self.min_x + (i * slice_width)
            slice_max_x = slice_min_x + slice_width
            for j in range(y_into):
                slice_min_y = self.min_y + (j * slice_height)
                slice_max_y = slice_min_y + slice_height
                slices.append(
                    BoundingBox(
                        min_x=round(Decimal(slice_min_x, context), 6),
                        max_x=round(Decimal(slice_max_x, context), 6),
                        min_y=round(Decimal(slice_min_y, context), 6),
                        max_y=round(Decimal(slice_max_y, context), 6),
                    )
                )

        return slices

    def to_shapely(self) -> Polygon:
        """Converts the bounding box to a shapely `Polygon`.

        Args:
            `None`

        Returns:
            (`Polygon`): The polygon.
        """
        return box(
            float(str(self.min_x)),
            float(str(self.min_y)),
            float(str(self.max_x)),
            float(str(self.max_y)),
        )
