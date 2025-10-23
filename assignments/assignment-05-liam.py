import math
import random
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt = 0 
        self.running = True
        self.num_row = 0
        self.num_collumn = 0
        self.cell = []
        while self.num_row < 128:
            self.cell.append(0)
            self.num_row += 1
        self.cells = []
        while self.num_collumn < 72:
            self.cells.append(self.cell)
            self.num_collumn += 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        for num, row in enumerate(self.cells):
            for pos, i in enumerate(row):
                if i == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(pos * 10, num * 10, 10, 10))
                elif i == 2:
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(pos * 10, num * 10, 10, 10))
                elif i == 3:
                    pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos * 10, num * 10, 10, 10))
                else:
                    continue
                    

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
        self.cells = []
        for y in range(72):
            self.cell = []
            for x in range(128):
                self.cell.append(random.randrange(4))
            self.cells.append(self.cell)

    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(30) * 0.001

        pygame.quit()

game = Game()
game.run()
