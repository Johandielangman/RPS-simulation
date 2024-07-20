import pygame
from pygame.math import Vector2
import random

from constants import (
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    SPRITE_WIDTH,
    SPRITE_HEIGHT
)


class GameObject:
    def __init__(self, object_type, speed):
        self.object_type = object_type
        self.speed = speed
        self.image = pygame.image.load(f'{object_type}.bmp').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SPRITE_WIDTH, SPRITE_HEIGHT))
        self.pos = Vector2(random.randint(0, CANVAS_WIDTH - SPRITE_WIDTH), random.randint(0, CANVAS_HEIGHT - SPRITE_HEIGHT))
        self.rect = self.image.get_rect(topleft=self.pos)
        self.direction = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

    def move(self):
        self.pos += self.direction * self.speed
        if self.pos.x < 0 or self.pos.x > CANVAS_WIDTH - SPRITE_WIDTH:
            self.direction.x *= -1
        if self.pos.y < 0 or self.pos.y > CANVAS_HEIGHT - SPRITE_HEIGHT:
            self.direction.y *= -1
        self.pos.x = max(0, min(self.pos.x, CANVAS_WIDTH - SPRITE_WIDTH))
        self.pos.y = max(0, min(self.pos.y, CANVAS_HEIGHT - SPRITE_HEIGHT))
        self.rect.topleft = self.pos

    def change_type(self, new_type):
        if self.object_type != new_type:
            self.object_type = new_type
            self.image = pygame.image.load(f'{new_type}.bmp').convert_alpha()
            self.image = pygame.transform.scale(self.image, (SPRITE_WIDTH, SPRITE_HEIGHT))
            return True
        return False

def play_rps(obj1, obj2):
    if obj1.object_type == obj2.object_type:
        return None
    elif (
        (obj1.object_type == 'rock' and obj2.object_type == 'scissors') or
        (obj1.object_type == 'scissors' and obj2.object_type == 'paper') or
        (obj1.object_type == 'paper' and obj2.object_type == 'rock')
    ):
        return obj1.object_type
    else:
        return obj2.object_type