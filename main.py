import pygame

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player_1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if CircleShape.collision_check(asteroid, player_1) == True:
                print("Game over!")
                return

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        clock.tick(MAX_FPS)
        dt = (clock.tick(MAX_FPS) / 1000)

if __name__ == "__main__":
    main()