import dataclasses
from arcade import color


@dataclasses.dataclass()
class ScreenConstants:
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 500
    SCREEN_TITLE = "Snake"


@dataclasses.dataclass()
class SnakeProperties:
    SNAKE_HEIGHT = 20
    SNAKE_WIDTH = 20
    VELOCITY = 2
    COLOR = color.GREEN
