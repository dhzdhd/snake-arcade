import arcade
import dataclasses


@dataclasses.dataclass()
class Position:
    x: int
    y: int


class Snake(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
