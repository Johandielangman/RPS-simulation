import pygame
import random
from pygame.math import Vector2
from constants import (
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    SPRITE_WIDTH,
    SPRITE_HEIGHT
)


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    background = pygame.image.load('background.bmp').convert()

    # Load collision sound
    collision_sound = pygame.mixer.Sound('collision.mp3')

    player = None
    objects = [GameObject(random.choice(['rock', 'paper', 'scissors']), random.uniform(1, 3)) for _ in range(30)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if player is None and (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            player = GameObject(random.choice(['rock', 'paper', 'scissors']), 5)
            player.pos = Vector2(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            player.rect.center = player.pos

        screen.blit(background, (0, 0))

        # Move and draw objects, check for collisions
        for obj in objects:
            obj.move()
            screen.blit(obj.image, obj.rect.topleft)

            if player:
                if player.rect.colliderect(obj.rect):
                    winner = play_rps(player, obj)
                    if winner:
                        if winner == player.object_type:
                            if obj.change_type(winner):
                                collision_sound.play()
                        else:
                            if player.change_type(winner):
                                collision_sound.play()

            # Check collisions between objects
            for other_obj in objects:
                if obj != other_obj and obj.rect.colliderect(other_obj.rect):
                    winner = play_rps(obj, other_obj)
                    if winner:
                        if winner == obj.object_type:
                            if other_obj.change_type(winner):
                                collision_sound.play()
                        else:
                            if obj.change_type(winner):
                                collision_sound.play()

        if player:
            if keys[pygame.K_UP]:
                player.pos.y -= player.speed
            if keys[pygame.K_DOWN]:
                player.pos.y += player.speed
            if keys[pygame.K_LEFT]:
                player.pos.x -= player.speed
            if keys[pygame.K_RIGHT]:
                player.pos.x += player.speed

            player.pos.x = max(0, min(player.pos.x, CANVAS_WIDTH - SPRITE_WIDTH))
            player.pos.y = max(0, min(player.pos.y, CANVAS_HEIGHT - SPRITE_HEIGHT))
            player.rect.topleft = player.pos
            screen.blit(player.image, player.rect.topleft)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main_loop()
    pygame.quit()
