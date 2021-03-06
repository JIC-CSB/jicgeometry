"""Module for geometric operations.

The module contains two classes to perform geometric operations in 2D and 3D
space:

- :class:`jicgeometry.Point2D`
- :class:`jicgeometry.Point3D`

A 2D point can be generated using a pair of x, y coordinates.

>>> p1 = Point2D(3, 0)

Alternatively, a 2D point can be created from a sequence.

>>> l = [0, 4]
>>> p2 = Point2D(l)

The x and y coordinates can be accessed as properties or by their index.

>>> p1.x
3
>>> p1[0]
3

Addition and subtraction result in vector arithmetic.

>>> p1 + p2
<Point2D(x=3, y=4, dtype=int)>
>>> p1 - p2
<Point2D(x=3, y=-4, dtype=int)>

Scalar multiplication is supported.

>>> (p1 + p2) * 2
<Point2D(x=6, y=8, dtype=int)>

Scalar division uses true division and as a result always returns a 2D point of
``dtype`` ``float``.

>>> p1 / 2
<Point2D(x=1.50, y=0.00, dtype=float)>

It is possible to calculate the distance between two points.

>>> p1.distance(p2)
5.0

Points can also be treated as vectors.

>>> p3 = p1 + p2
>>> p3.unit_vector
<Point2D(x=0.60, y=0.80, dtype=float)>
>>> p3.magnitude
5.0

"""

import math

__version__ = "0.6.0"


class Point2D(object):
    """Class representing a point in 2D space."""

    def __init__(self, a1, a2=None):
        if a2 is None:
            # We assume that we have given a sequence with x, y coordinates.
            self.x, self.y = a1
        else:
            self.x = a1
            self.y = a2

        self._set_types()

    def _set_types(self):
        """Make sure that x, y have consistent types and set dtype."""
        # If we given something that is not an int or a float we raise
        # a RuntimeError as we do not want to have to guess if the given
        # input should be interpreted as an int or a float, for example the
        # interpretation of the string "1" vs the interpretation of the string
        # "1.0".
        for c in (self.x, self.y):
            if not (isinstance(c, int) or isinstance(c, float)):
                raise(RuntimeError('x, y coords should be int or float'))

        if isinstance(self.x, int) and isinstance(self.y, int):
            self._dtype = "int"
        else:
            # At least one value is a float so promote both to float.
            self.x = float(self.x)
            self.y = float(self.y)
            self._dtype = "float"

    @property
    def dtype(self):
        """Return the type of the x, y coordinates as a string."""
        return self._dtype

    @property
    def magnitude(self):
        """Return the magnitude when treating the point as a vector."""
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def unit_vector(self):
        """Return the unit vector."""
        return Point2D(self.x / self.magnitude, self.y / self.magnitude)

    def distance(self, other):
        """Return distance to the other point."""
        tmp = self - other
        return tmp.magnitude

    def __repr__(self):
        s = "<Point2D(x={}, y={}, dtype={})>"
        if self.dtype == "float":
            s = "<Point2D(x={:.2f}, y={:.2f}, dtype={})>"
        return s.format(self.x, self.y, self.dtype)

    def __eq__(self, other):
        if self.dtype != other.dtype:
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point2D(self.x * other, self.y * other)

    def __div__(self, other):
        return self * (1/float(other))

    def __truediv__(self, other):
        return self.__div__(other)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise(IndexError())

    def __iter__(self):
        return iter([self.x, self.y])

    def astype(self, dtype):
        """Return a point of the specified dtype."""
        if dtype == "int":
            return Point2D(int(round(self.x, 0)), int(round(self.y, 0)))
        elif dtype == "float":
            return Point2D(float(self.x), float(self.y))
        else:
            raise(RuntimeError("Invalid dtype: {}".format(dtype)))

    def astuple(self):
        """Return the x, y coordinates as a tuple."""
        return self.x, self.y


class Point3D(object):
    """Class representing a point in 3D space."""

    def __init__(self, a1, a2=None, a3=None):
        if a2 is not None and a3 is not None:
            self.x, self.y, self.z = a1, a2, a3
        else:
            self.x, self.y, self.z = a1

        self._set_types()

    def _set_types(self):
        """Make sure that x, y, z have consistent types and set dtype."""
        # If we given something that is not an int or a float we raise
        # a RuntimeError as we do not want to have to guess if the given
        # input should be interpreted as an int or a float, for example the
        # interpretation of the string "1" vs the interpretation of the string
        # "1.0".
        for c in (self.x, self.y, self.z):
            if not (isinstance(c, int) or isinstance(c, float)):
                raise(RuntimeError('x, y coords should be int or float'))

        if (isinstance(self.x, int)
                and isinstance(self.y, int) and isinstance(self.z, int)):
            self._dtype = "int"
        else:
            # At least one value is a float so promote both to float.
            self.x = float(self.x)
            self.y = float(self.y)
            self.z = float(self.z)
            self._dtype = "float"

    @property
    def dtype(self):
        """Return the type of the x, y coordinates as a string."""
        return self._dtype

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __repr__(self):
        s = "<Point3D(x={}, y={}, z={}, dtype={})>"
        if self.dtype == "float":
            s = "<Point2D(x={:.2f}, y={:.2f}, z={:.2f}, dtype={})>"
        return s.format(self.x, self.y, self.z, self.dtype)

    def __eq__(self, other):
        if self.dtype != other.dtype:
            return False
        return (self.x == other.x
                and self.y == other.y
                and self.z == other.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        return self * (1/float(other))

    def __truediv__(self, other):
        return self.__div__(other)

    def __len__(self):
        return 3

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise(IndexError())

    @property
    def magnitude(self):
        """Return the magnitude when treating the point as a vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def unit_vector(self):
        """Return the unit vector."""
        return Point3D(self.x / self.magnitude,
                       self.y / self.magnitude,
                       self.z / self.magnitude)

    def distance(self, other):
        """Return distance to the other point."""
        tmp = self - other
        return tmp.magnitude

    def astype(self, dtype):
        """Return a point of the specified dtype."""
        if dtype == "int":
            return Point3D(int(round(self.x, 0)),
                           int(round(self.y, 0)),
                           int(round(self.z, 0)))
        elif dtype == "float":
            return Point3D(float(self.x), float(self.y), float(self.z))
        else:
            raise(RuntimeError("Invalid dtype: {}".format(dtype)))

    def astuple(self):
        """Return the x, y coordinates as a tuple."""
        return self.x, self.y, self.z
