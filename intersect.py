"""
Draw rectangles
(driver program for rects.py)
"""
import graphics.graphics
import argparse
import rect

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800


def cli():
    """Command line arguments for drawing two rectangles"""
    parser = argparse.ArgumentParser("Intersect rectangles")
    parser.add_argument("--display", "-d",  action="store_true")
    parser.add_argument(
        "ll_x1", type=int,
        help="X coordinate (in pixels) of lower left corner, first rect")
    parser.add_argument(
        "ll_y1", type=int,
        help="Y coordinate (in pixels) of lower left corner, first rect")
    parser.add_argument(
        "ur_x1", type=int,
        help="X coordinate (in pixels) of upper right corner, first rect")
    parser.add_argument(
        "ur_y1", type=int,
        help="Y coordinate (in pixels) of upper right corner, first rect")
    parser.add_argument(
        "ll_x2", type=int,
        help="X coordinate (in pixels) of lower left corner, second rect")
    parser.add_argument(
        "ll_y2", type=int,
        help="Y coordinate (in pixels) of lower left corner, second rect")
    parser.add_argument(
        "ur_x2", type=int,
        help="X coordinate (in pixels) of upper right corner, second rect")
    parser.add_argument(
        "ur_y2", type=int,
        help="Y coordinate (in pixels) of upper right corner, second rect")
    args = parser.parse_args()
    return args


def draw_rect(canvas, rect, color="black"):
    """Draw the rectangle on the canvas"""
    log.debug("Drawing {}".format(repr(rect)))
    ll_view = graphics.graphics.Point(rect.ll.x, rect.ll.y)
    ur_view = graphics.graphics.Point(rect.ur.x, rect.ur.y)
    view = graphics.graphics.Rectangle(ll_view, ur_view)
    view.setFill(color)
    view.draw(canvas)


def main():
    """Draw two rectangles on a canvas"""
    args = cli()
    r1 = rect.Rect(
        rect.Point(args.ll_x1, args.ll_y1),
        rect.Point(args.ur_x1, args.ur_y1))
    log.info("Rectangle {}".format(r1))
    r2 = rect.Rect(
        rect.Point(args.ll_x2, args.ll_y2),
        rect.Point(args.ur_x2, args.ur_y2))
    log.info("Rectangle {}".format(r2))
    if args.display:
        canvas = graphics.graphics.GraphWin("Rects", CANVAS_WIDTH, CANVAS_HEIGHT)
        draw_rect(canvas, r1, color="red")
        draw_rect(canvas, r2, color="blue")
        input("Press enter to intersect")
    r3 = r1.intersect(r2)
    print("Intersection: {}".format(r3))
    if args.display:
        draw_rect(canvas, r3, color="purple")
        input("Press enter to finish")
        canvas.close()


if __name__ == "__main__":
    main()
