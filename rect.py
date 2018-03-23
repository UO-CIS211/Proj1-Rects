"""
Rectangles:  Compute overlapping region of two rectangles.
  Point(x: number, y: number):  Cartesian coordinate pair
  Rect(ll: Point, ur: Pont): A rectangle defined by lower left
     and upper right coordinates
     Rect.overlaps(other: Rect) -> boolean:  True if non-empty overlap
     Rect.intersect(other: Rect) -> Rect:
        region of intersection if non-empty,
        or empty Rect from 0,0 to 0,0 if not Rect.overlaps(other)

CIS 211 Project 1
Author:  FIXME (your name here)
UO email: FIXME
"""
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Point(object):
    """A point is an ordered pair, (x,y)"""

    def __init__(self, x: int, y: int):
        assert isinstance(x,int) and isinstance(y, int)
        self.x = x
        self.y = y
        log.debug("Created Point {}".format(repr(self)))

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y


class Rect(object):
    """A rectangle identified by its lower left
    and upper right corners.
    """

    def __init__(self, ll, ur):
        """Initialize rectangle with ll and ur as corners."""
        log.debug("Rect from ll {}, ur {}".format(repr(ll), repr(ur)))
        # Ensure ll really is lower left and ur really is upper right
        self.ll = Point(min(ll.x, ur.x), min(ll.y, ur.y))
        log.debug("ll will be {}".format(self.ll))
        self.ur = Point(max(ll.x, ur.x), max(ll.y, ur.y))
        log.debug("ur will be {}".format(self.ur))
        log.debug("Created rect {}".format(repr(self)))

    def __repr__(self):
        return "Rect({},{})".format(repr(self.ll), repr(self.ur))

    def __str__(self):
        return "Rect({},{})".format(self.ll, self.ur)

    def __eq__(self, other: 'Rect'):
        return self.ll == other.ll and self.ur == other.ur

    def overlaps(self, other):
        if self.ur.x <= other.ll.x:
            # self is to the left of other
            return False
        if self.ur.y <= other.ll.y:
            # self is below other
            return False
        if self.ll.x >= other.ur.x:
            # self is to the right of other
            return False
        if self.ll.y >= other.ur.y:
            # self is above other
            return False
        return True

    def intersect(self, other: 'Rect'):
        """Region of overlap, or (0,0),(0,0) if none"""
        if self.overlaps(other):
            ll = Point(max(self.ll.x, other.ll.x),
                       max(self.ll.y, other.ll.y))
            ur = Point(min(self.ur.x, other.ur.x),
                       min(self.ur.y, other.ur.y))
            return Rect(ll, ur)
        else:
            return Rect(Point(0, 0), Point(0, 0))
