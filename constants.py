# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame
import os
from typing import (
    Union
)
from dotenv import load_dotenv
load_dotenv()

# =======================// GAME SETTINGS //======================= #

WINDOW_TITLE: str = os.getenv('WINDOW_TITLE', 'Rock Paper Scissors')

MIN_SPEED: int = int(os.getenv('MIN_SPEED', 1))
MAX_SPEED: int = int(os.getenv('MAX_SPEED', 3))

NUM_PLAYERS: int = int(os.getenv('NUM_PLAYERS', 30))
GAME_FPS: int = int(os.getenv('GAME_FPS', 60))
FONT_COLOR: tuple[int, int, int] = (255, 255, 255)

FONT_SIZE: int = int(os.getenv('FONT_SIZE', 24))
TEXT_PADDING: int = int(os.getenv('TEXT_PADDING', 10))

DARK_GREY: str = "#646250"

# =======================// DIMENSION SETTINGS //======================= #

SPRITE_WIDTH: int = int(os.getenv('SPRITE_WIDTH', 40))
SPRITE_HEIGHT: int = int(os.getenv('SPRITE_HEIGHT', 40))

CANVAS_WIDTH: int = int(os.getenv('CANVAS_WIDTH', 1280))
CANVAS_HEIGHT: int = int(os.getenv('CANVAS_HEIGHT', 720))


# =======================// GENERAL PATHS //======================= #

RESOURCES_FOLDER_PATH: str = os.path.join(os.path.dirname(__file__), 'resources')

BMP_FOLDER_PATH: str = os.path.join(RESOURCES_FOLDER_PATH, 'bmp')
SOUND_FOLDER_PATH: str = os.path.join(RESOURCES_FOLDER_PATH, 'sound')
FONTS_FOLDER_PATH: str = os.path.join(RESOURCES_FOLDER_PATH, 'fonts')

# =======================// IMAGES//======================= #

# 🦗 Background
BACKGROUND_IMAGE_PATH: str = os.path.join(BMP_FOLDER_PATH, 'background.bmp')

# 🗻 Rock
ROCK_IMAGE_PATH: str = os.path.join(BMP_FOLDER_PATH, 'rock.bmp')

# 📃 Paper
PAPER_IMAGE_PATH: str = os.path.join(BMP_FOLDER_PATH, 'paper.bmp')

# ✂ Scissors
SCISSORS_IMAGE_PATH: str = os.path.join(BMP_FOLDER_PATH, 'scissors.bmp')

FAVICON_PATH: str = os.path.join(RESOURCES_FOLDER_PATH, 'favicon.ico')


class PG_IMAGES:
    BACKGROUND: Union[pygame.Surface, None] = None
    ROCK: Union[pygame.Surface, None] = None
    PAPER: Union[pygame.Surface, None] = None
    SCISSORS: Union[pygame.Surface, None] = None
    FAVICON: Union[pygame.Surface, None] = None


# Collection of images
def load_images() -> object:
    pg_images: PG_IMAGES = PG_IMAGES()
    pg_images.BACKGROUND = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
    pg_images.FAVICON = pygame.image.load(FAVICON_PATH).convert_alpha()
    pg_images.ROCK = pygame.transform.scale(
        surface=pygame.image.load(
            ROCK_IMAGE_PATH
        ).convert_alpha(),
        size=(
            SPRITE_WIDTH,
            SPRITE_HEIGHT
        )
    )
    pg_images.PAPER = pygame.transform.scale(
        surface=pygame.image.load(
            PAPER_IMAGE_PATH
        ).convert_alpha(),
        size=(
            SPRITE_WIDTH,
            SPRITE_HEIGHT
        )
    )
    pg_images.SCISSORS = pygame.transform.scale(
        surface=pygame.image.load(
            SCISSORS_IMAGE_PATH
        ).convert_alpha(),
        size=(
            SPRITE_WIDTH,
            SPRITE_HEIGHT
        )
    )

    return pg_images

# =======================// SOUNDS //======================= #


# Collision sound
COLLISION_SOUND_PATH: str = os.path.join(SOUND_FOLDER_PATH, 'collision.mp3')


class PG_SOUNDS:
    COLLISION: Union[pygame.mixer.Sound, None] = None


# Collection of sounds
def load_sounds() -> object:
    pg_sounds: PG_SOUNDS = PG_SOUNDS()
    pg_sounds.COLLISION = pygame.mixer.Sound(COLLISION_SOUND_PATH)
    return pg_sounds


# =======================// FONTS //======================= #

UBUNTU_BOLD_FONT_PATH: str = os.path.join(FONTS_FOLDER_PATH, 'Ubuntu-Bold.ttf')


class PG_FONTS:
    UBUNTU_BOLD: Union[pygame.font.Font, None] = None


def load_fonts():
    pg_fonts: PG_FONTS = PG_FONTS()
    pg_fonts.UBUNTU_BOLD = pygame.font.Font(UBUNTU_BOLD_FONT_PATH, FONT_SIZE)
    return pg_fonts
