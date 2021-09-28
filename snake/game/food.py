import arcade
import random
from snake.constants import ScreenConstants
from snake.game.snake import SnakeHead


class Food(arcade.Sprite):
    def __init__(self, sprite_list: arcade.SpriteList) -> None:
        self.sprite_list = sprite_list

        super().__init__(
            filename="snake/assets/sprites/snake_body.png",
            center_x=random.randint(30, ScreenConstants.SCREEN_WIDTH - 30),
            center_y=random.randint(30, ScreenConstants.SCREEN_HEIGHT - 30),
        )

    def on_update(self, delta_time: float = 1 / 60):
        if arcade.check_for_collision_with_list(self, sprite_list=self.sprite_list):
            self.kill()
            create_food(self.sprite_list)


def create_food(sprite_list: arcade.SpriteList):
    food = Food(sprite_list)
    food.draw()
