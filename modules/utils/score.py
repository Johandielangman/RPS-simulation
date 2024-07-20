# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame
from typing import (
    Dict,
    List,
    TYPE_CHECKING
)
from constants import (
    TEXT_PADDING
)
if TYPE_CHECKING:
    from constants import (
        PG_IMAGES
    )
    from modules.utils.ternary import TernaryDiagram


class ScoreBoard:
    def __init__(
        self,
        font: pygame.font.Font,
        font_color: tuple[int, int, int],
        images: 'PG_IMAGES',
        ternary_diagram: 'TernaryDiagram'
    ) -> None:
        self.font = font
        self.font_color = font_color
        self.images = images
        self.ternary_diagram = ternary_diagram
        self.counts: Dict[str, int] = {
            'rock': 0,
            'paper': 0,
            'scissors': 0
        }
        self.percentages: Dict[str, float] = {
            'rock': 0.0,
            'paper': 0.0,
            'scissors': 0.0
        }
        self.text_surfaces: Dict[str, pygame.Surface] = {}
        self.update_text_surfaces()
        self.line_height = max(
            self.font.get_linesize(),
            self.images.ROCK.get_height()
        )
        self.padding: int = TEXT_PADDING
        self.image_padding: int = TEXT_PADDING // 2

    def update_counts(
        self,
        players: List[pygame.sprite.Sprite]
    ) -> None:
        rock_count: int = sum(1 for player in players if player.player_type == 'rock')
        paper_count: int = sum(1 for player in players if player.player_type == 'paper')
        scissors_count: int = sum(1 for player in players if player.player_type == 'scissors')
        total_count: int = sum([rock_count, paper_count, scissors_count])

        self.counts = {
            'rock': rock_count,
            'paper': paper_count,
            'scissors': scissors_count
        }
        self.percentages = {
            'rock': rock_count / total_count * 100 if total_count > 0 else 0,
            'paper': paper_count / total_count * 100 if total_count > 0 else 0,
            'scissors': scissors_count / total_count * 100 if total_count > 0 else 0
        }

        self.update_text_surfaces()
        self.ternary_diagram.add_point(
            rock=rock_count,
            paper=paper_count,
            scissors=scissors_count
        )

    def update_text_surfaces(self) -> None:
        self.text_surfaces = {
            'rock': self.font.render(f'{self.counts["rock"]:>3} ({self.percentages["rock"]:.1f}%)', True, self.font_color),
            'paper': self.font.render(f'{self.counts["paper"]:>3} ({self.percentages["paper"]:.1f}%)', True, self.font_color),
            'scissors': self.font.render(f'{self.counts["scissors"]:>3} ({self.percentages["scissors"]:.1f}%)', True, self.font_color)
        }

    def draw(
        self,
        surface: pygame.Surface
    ) -> None:
        for i, (key, text_surface) in enumerate(self.text_surfaces.items()):
            y_position: int = self.padding + i * (self.line_height + self.padding)

            # Draw the image
            image: pygame.Surface = getattr(self.images, key.upper())
            image_rect = image.get_rect(midleft=(self.padding, y_position + self.line_height // 2))
            surface.blit(source=image, dest=image_rect)

            # Draw the text
            text_x = image_rect.right + self.image_padding
            text_y = y_position + (self.line_height - text_surface.get_height()) // 2
            surface.blit(source=text_surface, dest=(text_x, text_y))

        # Draw the ternary diagram
        self.ternary_diagram.draw(surface)
