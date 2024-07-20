# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame
from pygame.math import Vector2
import random
from typing import (
    TYPE_CHECKING
)

from constants import (
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    SPRITE_WIDTH,
    SPRITE_HEIGHT,
    MIN_SPEED,
    load_images,
    load_sounds
)
if TYPE_CHECKING:
    from constants import (
        PG_IMAGES,
        PG_SOUNDS
    )


class PlayerObject:
    def __init__(
        self,
        player_type: str,
        player_speed: int = MIN_SPEED
    ) -> None:
        self.player_type = player_type
        self.player_speed = player_speed
        self.PG_IMAGES: 'PG_IMAGES' = load_images()
        self.PG_SOUNDS: 'PG_SOUNDS' = load_sounds()

        self.load_image()
        self.init_pos()
        self.init_rect()
        self.init_direction()

    def load_image(self) -> None:
        match self.player_type:
            case 'rock':
                self.image: pygame.Surface = self.PG_IMAGES.ROCK
            case 'paper':
                self.image: pygame.Surface = self.PG_IMAGES.PAPER
            case 'scissors':
                self.image: pygame.Surface = self.PG_IMAGES.SCISSORS
            case _:
                raise ValueError('Invalid player type')

    def init_pos(self) -> None:
        MIN_X: int = 0
        MAX_X: int = CANVAS_WIDTH - SPRITE_WIDTH

        MIN_Y: int = 0
        MAX_Y: int = CANVAS_HEIGHT - SPRITE_HEIGHT

        self.pos: Vector2 = Vector2(
            x=random.randint(MIN_X, MAX_X),
            y=random.randint(MIN_Y, MAX_Y)
        )

    def init_rect(self) -> None:
        self.rect: pygame.Rect = self.image.get_rect(
            topleft=self.pos
        )

    def init_direction(self) -> None:
        self.direction: Vector2 = Vector2(
            x=random.uniform(-1, 1),
            y=random.uniform(-1, 1)
        ).normalize()

    def edge_collision(self) -> None:
        MAX_X: int = CANVAS_WIDTH - SPRITE_WIDTH
        MAX_Y: int = CANVAS_HEIGHT - SPRITE_HEIGHT

        # Check if the player is at the edge of the screen, if so, change direction
        if (
            self.pos.x < 0 or
            self.pos.x > MAX_X
        ):
            self.direction.x *= -1
        if (
            self.pos.y < 0 or
            self.pos.y > MAX_Y
        ):
            self.direction.y *= -1

        # Clamp the position to the screen
        self.pos.x = max(0, min(self.pos.x, MAX_X))
        self.pos.y = max(0, min(self.pos.y, MAX_Y))

    def update_rect(self) -> None:
        self.rect.topleft = self.pos

    def play(self):
        self.pos += self.direction * self.player_speed
        self.edge_collision()
        self.update_rect()

    def change_type(
        self,
        new_type: str
    ) -> bool:
        if self.player_type != new_type:
            self.PG_SOUNDS.COLLISION.play()
            self.player_type = new_type
            self.load_image()
            return True
        return False
