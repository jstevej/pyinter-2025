# import math
# import random
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt = 0 # elapsed time between frames, in seconds
        self.running = True
        self.sprites = pygame.sprite.Group()

        # create your sprites here, then add them to the sprites group
        #
        # my_sprite = MySprite()
        # self.sprites.add(my_sprite)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False

        return True

    def handle_key_presses(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            print("a was pressed")

    def update(self):
        self.sprites.update(self.dt)

    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.handle_key_presses()
            self.update()
            self.draw()
            self.dt = self.clock.tick(30) * 0.001 # get elapsed time in seconds

        pygame.quit()

game = Game()
game.run()
