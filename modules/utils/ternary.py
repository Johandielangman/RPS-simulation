# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame
import math
from typing import (
    List,
    Tuple,
    TYPE_CHECKING
)
from constants import (
    FONT_COLOR,
    DOT_SIZE,
    COLOR_RED,
    load_fonts
)
if TYPE_CHECKING:
    from constants import (
        PG_FONTS
    )


class TernaryDiagram:
    def __init__(
        self,
        size: int,
        position: Tuple[int, int]
    ) -> None:
        self.size = size
        self.position = position
        self.points: List[Tuple[float, float, float]] = []
        self.max_points: int = 500

        self.PG_FONTS: 'PG_FONTS' = load_fonts()

    def add_point(
        self,
        rock: float,
        paper: float,
        scissors: float
    ) -> None:
        total: int = sum([rock, paper, scissors])
        if total > 0:
            percentages = (
                rock / total,
                paper / total,
                scissors / total
            )
            self.points.append(percentages)
            if len(self.points) > self.max_points:
                self.points.pop(0)

    def barycentric_to_cartesian(
        self,
        a: float,
        b: float,
        c: float
    ) -> Tuple[float, float]:
        x = self.size * (c + b / 2) / (a + b + c)
        y = self.size * (math.sqrt(3) / 2) * b / (a + b + c)
        return (x, self.size - y)  # Invert y-coordinate

    def p_left(
        self,
        px: int = 0,
        py: int = 0
    ) -> Tuple[int, int]:
        pos_x, pos_y = self.position
        return (pos_x + px, pos_y + self.size + py)

    def p_right(
        self,
        px: int = 0,
        py: int = 0
    ) -> Tuple[int, int]:
        pos_x, pos_y = self.position
        return (pos_x + self.size + px, pos_y + self.size + py)

    def p_top(
        self,
        px: int = 0,
        py: int = 0
    ) -> Tuple[int, int]:
        pos_x, pos_y = self.position
        return (pos_x + self.size / 2 + px, pos_y + py)

    def draw_triangle(
        self,
        surface: pygame.Surface
    ) -> None:
        pygame.draw.polygon(
            surface,
            FONT_COLOR,
            [
                self.p_left(),
                self.p_right(),
                self.p_top()
            ],
            1
        )

    def draw(
        self,
        surface: pygame.Surface
    ) -> None:
        self.draw_triangle(surface)
        post_x, post_y = self.position

        for point in self.points:
            x, y = self.barycentric_to_cartesian(*point)
            pygame.draw.circle(
                surface,
                COLOR_RED,
                (
                    int(post_x + x),
                    int(post_y + y)
                ),
                DOT_SIZE
            )

        labels: pygame.font.Font = self.PG_FONTS.UBUNTU_BOLD
        rock_text = labels.render("Rock", True, FONT_COLOR)
        paper_text = labels.render("Paper", True, FONT_COLOR)
        scissors_text = labels.render("Scissors", True, FONT_COLOR)

        surface.blit(rock_text, self.p_left(px=-30))
        surface.blit(scissors_text, self.p_right())
        surface.blit(paper_text, self.p_top(px=-30, py=-30))
