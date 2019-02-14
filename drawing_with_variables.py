

import arcade


WIDTH = 640
HEIGHT = 480
# get user input for x , y and radius
x = float(input("enter x location:"))
y = 350
radius = 100

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()
