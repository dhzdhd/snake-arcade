import arcade

from snake.game import game

if __name__ == "__main__":
    window = game.Game()
    window.setup()
    arcade.run()
