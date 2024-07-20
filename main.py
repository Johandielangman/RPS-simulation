# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~


import pygame
import random
from modules.utils.ternary import TernaryDiagram
from modules.Object.GameObjects import PlayerObject
from modules.utils.score import ScoreBoard
from modules.utils.rps import (
    play_rps,
    handle_winner
)
from typing import (
    TYPE_CHECKING
)
from constants import (
    CANVAS_WIDTH,
    WINDOW_TITLE,
    CANVAS_HEIGHT,
    MIN_SPEED,
    MAX_SPEED,
    NUM_PLAYERS,
    GAME_FPS,
    FONT_COLOR,
    COLOR_DARK_GREY,
    TERNARY_SIZE,
    load_images,
    load_fonts
)
if TYPE_CHECKING:
    from constants import (
        PG_IMAGES,
        PG_FONTS
    )


def main_loop():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        size=(CANVAS_WIDTH, CANVAS_HEIGHT)
    )
    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption(WINDOW_TITLE)

    pg_images: 'PG_IMAGES' = load_images()
    pg_fonts: 'PG_FONTS' = load_fonts()

    pygame.display.set_icon(pg_images.FAVICON)

    # Initialize TernaryDiagram
    ternary_diagram = TernaryDiagram(
        size=TERNARY_SIZE,
        position=(TERNARY_SIZE * 0.5, CANVAS_HEIGHT - TERNARY_SIZE * 1.5),
    )

    # Initialize ScoreBoard
    score_board = ScoreBoard(
        font=pg_fonts.UBUNTU_BOLD,
        font_color=FONT_COLOR,
        images=pg_images,
        ternary_diagram=ternary_diagram
    )

    running: bool = True

    all_players: list[PlayerObject] = [
        PlayerObject(
            player_type=random.choice(
                [
                    'rock',
                    'paper',
                    'scissors'
                ]
            ),
            player_speed=random.uniform(MIN_SPEED, MAX_SPEED)
        ) for _ in range(NUM_PLAYERS)]

    # Initialize scoreboard
    score_board.update_counts(all_players)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # screen.blit(pg_images.BACKGROUND, (0, 0))
        screen.fill(COLOR_DARK_GREY)

        for player_1 in all_players:
            player_1.play()
            screen.blit(
                source=player_1.image,
                dest=player_1.rect.topleft
            )

            for player_2 in all_players:
                if (
                    player_1 != player_2 and
                    player_1.rect.colliderect(player_2.rect)
                ):
                    winner: str = play_rps(
                        player_1=player_1,
                        player_2=player_2
                    )
                    handle_winner(
                        winner=winner,
                        player_1=player_1,
                        player_2=player_2
                    )

                    # Update scoreboard
                    score_board.update_counts(all_players)

        # Draw scoreboard
        score_board.draw(screen)

        pygame.display.flip()
        clock.tick(GAME_FPS)


if __name__ == "__main__":
    main_loop()
    pygame.quit()
