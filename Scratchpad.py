import time
import graphics
# import random


def main():
        window1 = graphics.GraphWin("Main Window", 500, 500)
        tri_p1 = graphics.Point(50, 450)
        tri_p2 = graphics.Point(250, 25)
        tri_p3 = graphics.Point(450, 450)
        ref_triangle = graphics.Polygon(tri_p1, tri_p2, tri_p3)
        ref_triangle.draw(window1)
        circle = graphics.Circle(graphics.Point(250, 300), 100)
        circle.setFill("black")
        circle.draw(window1)
        # eye = graphics.Oval()
        for flash in range(25):
            ref_triangle.setFill("red")
            circle.setFill("grey")
            time.sleep(.1)
            ref_triangle.setFill("blue")
            circle.setFill("black")
            time.sleep(.1)
            ref_triangle.setFill("green")
            circle.setFill("grey")
            time.sleep(.1)
            ref_triangle.setFill("yellow")
            circle.setFill("black")
            time.sleep(.1)








main()