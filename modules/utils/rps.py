# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame


def play_rps(
    player_1: pygame.sprite.Sprite,
    player_2: pygame.sprite.Sprite
) -> str:
    if player_1.player_type == player_2.player_type:
        return None
    elif (
        (
            player_1.player_type == 'rock' and
            player_2.player_type == 'scissors'
        ) or
        (
            player_1.player_type == 'scissors' and
            player_2.player_type == 'paper'
        ) or
        (
            player_1.player_type == 'paper' and
            player_2.player_type == 'rock'
        )
    ):
        return player_1.player_type
    else:
        return player_2.player_type


def handle_winner(
    winner: str,
    player_1: pygame.sprite.Sprite,
    player_2: pygame.sprite.Sprite
):
    if winner:
        if winner == player_1.player_type:
            player_2.change_type(winner)
        else:
            player_2.change_type(winner)
