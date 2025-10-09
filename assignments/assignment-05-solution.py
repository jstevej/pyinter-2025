import random
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

        self.num_rows = 128
        self.num_cols = 72
        self.cell_width = self.screen_width // self.num_rows
        self.cell_height = self.screen_height // self.num_cols
        self.cells = []
        for _ in range(self.num_rows):
            self.cells.append([0] * self.num_cols) # add a row of empty cells

    def draw(self):
        self.screen.fill((0, 0, 0)) # erase screen

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                color = None
                if self.cells[row][col] == 1:
                    color = (255, 0, 0)
                elif self.cells[row][col] == 2:
                    color = (0, 255, 0)
                elif self.cells[row][col] == 3:
                    color = (0, 0, 255)

                if color is not None:
                    x = row * self.cell_width
                    y = col * self.cell_height
                    rect = (x, y, self.cell_width, self.cell_height)
                    pygame.draw.rect(self.screen, color, rect)

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
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col] = random.randint(0, 3)

    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(30) * 0.001 # get elapsed time in seconds

        pygame.quit()

game = Game()
game.run()
