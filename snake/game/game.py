import arcade
from snake.constants import ScreenConstants, SnakeProperties
from snake.game.snake import SnakeHead, SnakeTail, SnakeBody
from typing import Union
from snake.game.food import Food


class Game(arcade.Window):
    collision: bool = False

    def __init__(self) -> None:
        super().__init__(
            ScreenConstants.SCREEN_WIDTH,
            ScreenConstants.SCREEN_HEIGHT,
            ScreenConstants.SCREEN_TITLE,
            center_window=True
        )

        self.sprite_list: arcade.SpriteList = None
        self.snake_head: SnakeHead = None
        self.snake_tail: SnakeTail = None
        self.food: Food = None

        arcade.enable_timings()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> None:
        self.sprite_list = arcade.SpriteList(use_spatial_hash=True)

        self.snake_head = SnakeHead(self.sprite_list)
        self.sprite_list.append(self.snake_head)

        self.snake_tail = SnakeTail()
        self.sprite_list.append(self.snake_tail)

        self.food = Food(self.sprite_list)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            str(int(arcade.get_fps())),
            10,
            ScreenConstants.SCREEN_HEIGHT - 15,
            arcade.color.GREEN,
        )
        self.sprite_list.draw()
        self.food.draw()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake_head.center_x += self.snake_head.change_x
        self.snake_head.center_y += self.snake_head.change_y

        self.sprite_list.update()

    def on_key_press(self, symbol: int, modifiers: int):
        self.snake_head.change_x = 0
        self.snake_head.change_y = 0

        if symbol == arcade.key.RIGHT:
            self.snake_head.angle = 270
            self.snake_head.change_x += SnakeProperties.VELOCITY
        if symbol == arcade.key.LEFT:
            self.snake_head.angle = 90
            self.snake_head.change_x -= SnakeProperties.VELOCITY
        if symbol == arcade.key.UP:
            self.snake_head.angle = 0
            self.snake_head.change_y += SnakeProperties.VELOCITY
        if symbol == arcade.key.DOWN:
            self.snake_head.angle = 180
            self.snake_head.change_y -= SnakeProperties.VELOCITY

