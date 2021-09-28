import arcade
import dataclasses
from typing import Union
from snake.constants import ScreenConstants


@dataclasses.dataclass()
class Position:
    x: int
    y: int


class SnakeHead(arcade.Sprite):
    def __init__(self, sprite_list: arcade.SpriteList):
        self.sprite_list = sprite_list

        super().__init__(
            filename="snake/assets/sprites/snake_head.png",
            center_x=ScreenConstants.SCREEN_WIDTH / 2,
            center_y=ScreenConstants.SCREEN_HEIGHT / 2,
        )

    def on_update(self, delta_time: float = 1 / 60):
        wall_collision(self)


class SnakeBody(arcade.Sprite):
    def __init__(self, center_x: int, center_y: int) -> None:
        super().__init__(
            filename="snake/assets/sprites/snake_body.png",
            center_x=center_x,
            center_y=center_y
        )


class SnakeTail(arcade.Sprite):
    def __init__(self):
        super().__init__(
            filename="snake/assets/sprites/snake_tail.png",
            center_x=ScreenConstants.SCREEN_WIDTH / 2,
            center_y=ScreenConstants.SCREEN_HEIGHT / 2 - 40,
        )


def wall_collision(snake_instance: Union[SnakeHead, SnakeTail, SnakeBody]) -> None:
    if snake_instance.center_x > ScreenConstants.SCREEN_WIDTH:
        snake_instance.center_x = 0
    if snake_instance.center_x < 0:
        snake_instance.center_x = ScreenConstants.SCREEN_WIDTH
    if snake_instance.center_y > ScreenConstants.SCREEN_HEIGHT:
        snake_instance.center_y = 0
    if snake_instance.center_y < 0:
        snake_instance.center_y = ScreenConstants.SCREEN_HEIGHT



