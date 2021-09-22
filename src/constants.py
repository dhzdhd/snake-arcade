import dataclasses
from arcade import color


@dataclasses.dataclass()
class ScreenConstants:
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
    SCREEN_TITLE = "Snake"


@dataclasses.dataclass()
class SnakeProperties:
    SNAKE_HEIGHT = 20
    SNAKE_WIDTH = 20
    VELOCITY = 10
    COLOR = color.GREEN


