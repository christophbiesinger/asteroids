import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # Player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for ob in updatable:
            ob.update(dt)

        for dr in drawable:
            dr.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player.position):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet.position):
                    asteroid.split()
                    bullet.kill()

        # rendering
        pygame.display.flip()
        
        # 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
