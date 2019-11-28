
 
import random
import arcade
import math
import os
import time

WIDTH = 800
HEIGHT = 600
SCREEN_TITLE = "Kungfu Chef"
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
dabbing_chef = arcade.load_texture('/home/robuntu/xia/classwork/acade/4733564_0.jpg')
chicken_leg = arcade.load_texture('/home/robuntu/xia/classwork/acade/image url.png')
egg = arcade.load_texture('/home/robuntu/xia/classwork/acade/image url (2).png')
beef = arcade.load_texture('/home/robuntu/xia/classwork/acade/image url (4).png')
chef_ninja = arcade.load_texture('/home/robuntu/xia/classwork/acade/chef_ninja_6830391.jpg')


class Food:

    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        self.y = (HEIGHT + 20)
        self.x = random.randrange(20, WIDTH - 20)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.COOL_GREY)

        self.food_list = []
        self.create_food()
        self.round = 0
        self.level = 1
        self.score = 0
        self.health = 3
        self.current_screen = "menu"
        self.tex_list = [chicken_leg, egg, beef]

    def create_food(self):

        food = Food()

        food.x = random.randrange(20, 780)
        food.y = (HEIGHT + 20)
        food.size = 20
        food.speed = 20
        clear_image = food.y








        self.food_list.append(food)


    def random_tex(self):
        num = random.randrange(3)




    def on_draw(self):
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, dabbing_chef)

        if self.current_screen == "menu":
            arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, chef_ninja)
            arcade.draw_text("Kungfu Chef", WIDTH / 2, HEIGHT - 120,
                             arcade.color.BLACK, font_size=60, anchor_x="center")

            arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2 + 25, 200, 60, arcade.color.ASH_GREY)
            arcade.draw_text("Play", WIDTH / 2, HEIGHT / 2,
                             arcade.color.BLACK, font_size=50, anchor_x="center")

            arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 3 + 10, 300, 60, arcade.color.ASH_GREY)
            arcade.draw_text("Instructions", WIDTH / 2, HEIGHT / 3 - 10,
                             arcade.color.BLACK, font_size=40, anchor_x="center")

        elif self.current_screen == "ins":
            arcade.set_background_color(arcade.color.WHITE_SMOKE)
            arcade.draw_text("Instructions", WIDTH / 2, HEIGHT / 3 * 2,
                             arcade.color.BLACK, font_size=60, anchor_x="center")

            arcade.draw_rectangle_filled(WIDTH - 40, 20, 80, 40, arcade.color.ASH_GREY)
            arcade. draw_text("Menu", WIDTH - 70 , 10, arcade.color.BLACK, font_size=20)

            arcade.draw_text("You are a chef of a restaurant, your job is to cut foods. ",
                             WIDTH / 2, HEIGHT / 2,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("Use your mouse to click on the dropping food.",
                             WIDTH / 2, HEIGHT / 2 - 30,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("For each food you have successfully clicked on, you will gain 10 score,",
                             WIDTH / 2, HEIGHT / 2 - 60,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("but for every click you miss, you will lose 10 score.",
                             WIDTH / 2, HEIGHT / 2 - 90,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("You have three lives, which means that",
                             WIDTH / 2, HEIGHT / 2 - 120,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("if the food hits the floor 3 times, the game is over.",
                             WIDTH / 2, HEIGHT / 2 - 150,
                             arcade.color.BLACK, font_size=20, anchor_x="center")

        elif self.current_screen == "play":
            arcade.set_background_color(arcade.color.ASH_GREY)
            num = self.random_tex
            num = random.randrange(3)
            if self.level == 1:
                tex = chicken_leg
                print(num)

            elif self.level == 2:
                tex = egg
                print(num)
            elif self.level == 3:
                tex = beef
                print(num)











            for food in self.food_list:
                arcade.draw_texture_rectangle(food.x, food.y, 60, 40, tex)
            score = int(self.score)
            arcade.draw_text(f"Socre: {score}", 10, HEIGHT - 30, arcade.color.BLACK, font_size=20)
            arcade.draw_text(f"Level: {self.level}", WIDTH - 80, HEIGHT - 30, arcade.color.BLACK, font_size=20)

            if self.health == 0:
                self.current_screen = "gameover"

        elif self.current_screen == "gameover":
            arcade.set_background_color(arcade.color.ASH_GREY)
            arcade.draw_text("GAME OVER!", 60, HEIGHT / 2 - 35, arcade.color.RED, font_size=100)
            arcade.draw_text(f"Score: {self.score}", WIDTH / 2, HEIGHT / 3 + 10,
                             arcade.color.BLACK, font_size=30)
            arcade.draw_text(f"Level:{self.level}", WIDTH / 2 - 100, HEIGHT / 3 + 10,
                             arcade.color.BLACK, font_size=30, anchor_x="center")
            arcade.draw_rectangle_filled(WIDTH - 40, 20, 80, 40, arcade.color.WHITE_SMOKE)
            arcade.draw_text("Menu", WIDTH - 70, 10, arcade.color.BLACK, font_size=20)




    def on_key_press(self,key, modifiers):

        if key == arcade.key.ESCAPE:
                self.current_screen = "menu"

    def update(self, delta_time):
        if self.current_screen == "play":
            for food in self.food_list:
                food.y -= food.speed * delta_time
                if food.y < -20:
                    food.reset_pos()
                    food.speed += 5
                    self.round += 1
                    self.health -= 1

            if self.round >= 50 * self.level:
                self.round = 0
                self.level += 1
                self.create_food()
                food.speed = 20
        elif self.current_screen == "menu":
            self.food_list = []
            self.create_food()
            self.round = 0
            self.level = 1
            self.score = 0
            self.health = 3

    def on_mouse_press(self, mouse_x: float, mouse_y: float, button: int, modifiers: int):
        if self.current_screen == "play":
            for food in self.food_list:
                run = mouse_x - food.x
                rise = mouse_y - (food.y + 2)
                distance = math.sqrt(run * run + rise * rise)

                if distance <= 23:
                    self.round += 1
                    food.reset_pos()
                    food.speed += 5
                    self.score += 15
            else:
                self.score -= 5

        if self.current_screen == "ins":
            if mouse_x >= (WIDTH - 80) and mouse_y <= 40:
                self.current_screen = "menu"

        if self.current_screen == "gameover":
            if mouse_x >= (WIDTH - 80) and mouse_y <= 40:
                self.current_screen = "menu"

        if self.current_screen == "menu":
            if mouse_x <= WIDTH / 2 + 100 and mouse_x >= WIDTH / 2 - 100 and mouse_y <= HEIGHT / 2 + 55 and mouse_y >= HEIGHT / 2 - 5:
                self.current_screen = "play"
            if mouse_x <= WIDTH / 2 + 150 and mouse_x >= WIDTH / 2 - 150 and mouse_y <= HEIGHT / 3 + 40 and mouse_y >= HEIGHT / 3 - 20:
                self.current_screen = "ins"


def main():
    window = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()


