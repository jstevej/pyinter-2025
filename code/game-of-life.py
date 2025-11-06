import random
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.num_cells_x = 256
        self.num_cells_y = 144
        self.cell_width = self.screen_width / self.num_cells_x
        self.cell_height = self.screen_height / self.num_cells_y
        self.cell_color = (0, 255, 255)
        self.grid = self.make_random_grid()
        self.new_grid = self.make_empty_grid()
        self.clock = pygame.time.Clock()
        self.dt = 0 # elapsed time between frames, in seconds
        self.running = True

    def compute_num_neighbors(self, x, y):
        num_neighbors = 0

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                nx = (x + dx) % self.num_cells_x
                ny = (y + dy) % self.num_cells_y
                if self.grid[ny][nx]:
                    num_neighbors += 1

        return num_neighbors

    def draw(self):
        self.screen.fill((0, 0, 0))
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                if self.grid[y][x]:
                    self.fill_cell(x, y, self.cell_color)
        pygame.display.flip()

    def fill_cell(self, x, y, color):
        rect = pygame.Rect(
            x * self.cell_width,
            y * self.cell_height,
            self.cell_width,
            self.cell_height
        )
        pygame.draw.rect(self.screen, color, rect)

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
        if keys_pressed[pygame.K_r]:
            self.reset()

    def make_empty_grid(self):
        empty_grid = []

        for _ in range(self.num_cells_y):
            col = []
            for _ in range(self.num_cells_x):
                col.append(0)
            empty_grid.append(col)

        return empty_grid

    def make_random_grid(self):
        random_grid = []

        for _ in range(self.num_cells_y):
            col = []
            for _ in range(self.num_cells_x):
                col.append(random.randrange(2))
            random_grid.append(col)

        return random_grid

    def reset(self):
        self.grid = self.make_random_grid()

    def update(self):
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                num_neighbors = self.compute_num_neighbors(x, y)

                self.new_grid[y][x] = self.grid[y][x]

                if self.grid[y][x]:
                    if num_neighbors < 2 or num_neighbors > 3:
                        self.new_grid[y][x] = 0
                else:
                    if num_neighbors == 3:
                        self.new_grid[y][x] = 1

        self.grid, self.new_grid = self.new_grid, self.grid


    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.handle_key_presses()
            self.update()
            self.draw()
            self.dt = self.clock.tick(2) * 0.001 # get elapsed time in seconds

        pygame.quit()

game = Game()
game.run()
