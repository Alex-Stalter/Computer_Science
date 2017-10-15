"""Written by Alex Stalter
The following code creates the Steam Logo that is surrounded by a blue circle, most of the parts are overlapping to
create the effect of one solid object
"""

import graphics


def main():
        window1 = graphics.GraphWin("Main Window", 500, 500)
        # this is the first main circle of the logo
        main_body = graphics.Circle(graphics.Point(250, 250), 175)
        main_body.setFill("black")
        main_body.setOutline("white")
        main_body.draw(window1)
        # arm1 is the line that comes onto the screen from the left side to form the left most part of the logo
        arm1 = graphics.Line(
                graphics.Point(50, 250),
                graphics.Point(200, 325)
        )
        arm1.setWidth(50)
        arm1.setOutline("white")
        arm1.setFill("white")
        arm1.draw(window1)
        # bot_top_connector is the connector between the bottom most cog of the logo and the top most cog o the logo
        bot_top_connector = graphics.Polygon(
            graphics.Point(240, 330),
            graphics.Point(190, 290),
            graphics.Point(270, 190),
            graphics.Point(370, 210),
        )
        bot_top_connector.setFill("white")
        bot_top_connector.setOutline("white")
        bot_top_connector.draw(window1)
        # outer bot is an outlined circle that forms the bottom part of the logo's cog
        outer_bot = graphics.Circle(graphics.Point(200, 325), 40)
        outer_bot.setOutline("white")
        outer_bot.setFill("black")
        outer_bot.setWidth(10)
        outer_bot.draw(window1)
        # inner_bot is the circle that forms the inner part of the bottom of the cog
        inner_bot = graphics.Circle(graphics.Point(200, 325), 25)
        inner_bot.setOutline("white")
        inner_bot.setFill("white")
        inner_bot.draw(window1)
        # outer top is the circle thatfroms the background of the upper cog
        outer_top = graphics.Circle(graphics.Point(320, 200), 50)
        outer_top.setOutline("white")
        outer_top.setWidth(50)
        outer_top.setFill("white")
        outer_top.draw(window1)
        # inner top is the black background behind the middle cog
        inner_top = graphics.Circle(graphics.Point(320, 200), 50)
        inner_top.setFill("black")
        inner_top.draw(window1)
        # middle_top is the center piece of the upper cog of the steam logo
        middle_top = graphics.Circle(graphics.Point(320, 200), 40)
        middle_top.setFill("white")
        middle_top.draw(window1)
        # outer main is the blue circle that surrounds the steam logo
        outer_main_circle = graphics.Circle(graphics.Point(250, 250), 180)
        outer_main_circle.setOutline("blue")
        outer_main_circle.setWidth(25)
        outer_main_circle.draw(window1)
        # getMouse allows the window to stay up until the user clicks in the window itself
        window1.getMouse()


main()