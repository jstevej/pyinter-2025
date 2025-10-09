import math
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
        self.density = 0.3
        self.color_change_prob = 0.001
        self.neighbor_range = 1
        self.vision_range = 2
        self.desired_similar_neighbors = 2
        # self.group_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.group_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        self.num_groups = len(self.group_colors)
        self.reset()
        self.clock = pygame.time.Clock()
        self.dt = 0 # elapsed time between frames, in seconds
        self.running = True
        #self.sprites = pygame.sprite.Group()

        # create your sprites here, then add them to the sprites group
        #
        # my_sprite = MySprite()
        # self.sprites.add(my_sprite)

    def compute_similar_neighbors(self, x, y):
        cell = self.grid[y][x]
        if cell is None:
            return 0, 0
        similar_neighbors = 0
        total_neighbors = 0
        for dy in range(-self.neighbor_range, self.neighbor_range + 1):
            for dx in range(-self.neighbor_range, self.neighbor_range + 1):
                if dy == 0 and dx == 0:
                    continue
                nx = (x + dx) % self.num_cells_x
                ny = (y + dy) % self.num_cells_y
                neighbor = self.grid[ny][nx]
                if neighbor is not None:
                    total_neighbors += 1
                    if neighbor == cell:
                        similar_neighbors += 1
        return similar_neighbors, total_neighbors

    def draw(self):
        self.screen.fill((0, 0, 0))
        #self.sprites.draw(self.screen)
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                cell = self.grid[y][x]
                if cell is not None:
                    color = self.group_colors[cell]
                    rect = pygame.Rect(
                        x * (self.screen_width / self.num_cells_x),
                        y * (self.screen_height / self.num_cells_y),
                        (self.screen_width / self.num_cells_x),
                        (self.screen_height / self.num_cells_y)
                    )
                    pygame.draw.rect(self.screen, color, rect)
        pygame.display.flip()

    def find_better_location(self, x, y, current_similar_neighbors):
        best_locations = []
        best_similar_neighbors = -1
        for dy in range(-self.vision_range, self.vision_range + 1):
            for dx in range(-self.vision_range, self.vision_range + 1):
                if dy == 0 and dx == 0:
                    continue
                nx = (x + dx) % self.num_cells_x
                ny = (y + dy) % self.num_cells_y
                if self.grid[ny][nx] is None:
                    similar_neighbors, _ = self.compute_similar_neighbors(nx, ny)
                    if similar_neighbors == best_similar_neighbors:
                        best_locations.append((nx, ny))
                    elif similar_neighbors > best_similar_neighbors:
                        best_locations = [(nx, ny)]
                        best_similar_neighbors = similar_neighbors
        if len(best_locations) > 0:
            return random.choice(best_locations)
        else:
            return None

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

    def reset(self):
        self.grid = []
        for _ in range(self.num_cells_y):
            row = []
            for _ in range(self.num_cells_x):
                if random.random() < self.density:
                    row.append(random.randrange(self.num_groups))
                else:
                    row.append(None)
            self.grid.append(row)

    def update(self):
        #self.sprites.update(self.dt)
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                cell = self.grid[y][x]
                if cell is None:
                    continue
                if random.random() < self.color_change_prob:
                    self.grid[y][x] = random.randrange(self.num_groups)
                similar_neighbors, _ = self.compute_similar_neighbors(x, y)
                if similar_neighbors < self.desired_similar_neighbors:
                    new_location = self.find_better_location(x, y, similar_neighbors)
                    if new_location is not None:
                        nx, ny = new_location
                        self.grid[ny][nx] = self.grid[y][x]
                        self.grid[y][x] = None

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
