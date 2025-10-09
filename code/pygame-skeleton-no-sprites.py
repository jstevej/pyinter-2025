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

    def draw(self):
        self.screen.fill((0, 0, 0)) # erase screen
        # do your drawing here
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

    def update(self):
        # update your game state here
        pass

    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(30) * 0.001 # get elapsed time in seconds

        pygame.quit()

game = Game()
game.run()
