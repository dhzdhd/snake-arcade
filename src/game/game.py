import arcade
from src.constants import ScreenConstants, SnakeProperties
from src.game.snake import Snake, Position


class Game(arcade.Window):
    def __init__(self) -> None:
        super().__init__(
            ScreenConstants.SCREEN_WIDTH,
            ScreenConstants.SCREEN_HEIGHT,
            ScreenConstants.SCREEN_TITLE,
            # resizable=True,
            center_window=True
        )

        self.sprite_list = None
        self.snake_head: Snake = None

        arcade.enable_timings()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self) -> None:
        self.sprite_list = arcade.SpriteList()

        self.snake_head = Snake(center_x=ScreenConstants.SCREEN_WIDTH / 2, center_y=ScreenConstants.SCREEN_HEIGHT / 2, )
        self.sprite_list.append(self.snake_head)

    def update(self, delta_time: float):
        self.wall_collision()

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(str(int(arcade.get_fps())), 10, ScreenConstants.SCREEN_HEIGHT - 15, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.snake_head.change_x, self.snake_head.change_y, SnakeProperties.SNAKE_WIDTH, SnakeProperties.SNAKE_HEIGHT, SnakeProperties.COLOR)

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.snake_head.change_x += SnakeProperties.VELOCITY

    def wall_collision(self) -> None:
        if self.snake_head.center_x > ScreenConstants.SCREEN_WIDTH:
            self.snake_head.center_x = 0
        if self.snake_head.center_x < 0:
            self.snake_head.center_x = ScreenConstants.SCREEN_WIDTH
        if self.snake_head.center_y > ScreenConstants.SCREEN_HEIGHT:
            self.snake_head.center_y = 0
        if self.snake_head.center_y < 0:
            self.snake_head.center_y = ScreenConstants.SCREEN_HEIGHT
