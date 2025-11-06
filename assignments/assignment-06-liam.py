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
        self.cell_width = 5
        self.cell_height = 5
        self.num_column = 256
        self.num_row = 144
        self.num_groups = 3
        self.density = 0.3
        self.neighbors_wanted = 2
        self.cells = []

        for _ in range(self.num_row):
            row = []
            for _ in range(self.num_column):
                if random.random() < self.density:
                    row.append(random.randrange(self.num_groups) + 1)
                else:
                    row.append(0)
            self.cells.append(row)
       

    def draw(self):
        self.screen.fill((0, 0, 0))
        for num, row in enumerate(self.cells):
            for pos, i in enumerate(row):
                if i == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(pos * self.cell_width, num * self.cell_height, self.cell_width, self.cell_height))
                elif i == 2:
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(pos * self.cell_width, num * self.cell_height, self.cell_width, self.cell_height))
                elif i == 3:
                    pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos * self.cell_width, num * self.cell_height, self.cell_width, self.cell_height))
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
    
    def check_neighbors(self, origin, y, x):
        # this doesn't need to be a class member
        self.similar_neighbors = 0
        
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                nx = (x+i) % self.num_column
                ny = (y+j) % self.num_row
                if self.cells[ny][nx] == origin:
                    self.similar_neighbors += 1
        
        return self.similar_neighbors

    def update(self):
        for y, row in enumerate(self.cells):
            for x, column in enumerate(row):
                # do you need to make sure this cell is occupied first?
                self.check_neighbors(column, y, x)
                if self.similar_neighbors >= 2:
                    continue
                else:
                    # this could be moved to its own function
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if i == 0 and j == 0:
                                # continue doesn't do anything here because there's no code after
                                # the if/else
                                continue
                            else:
                                if self.cells[y][x] == 0:
                                    # this condition seems useless because if we get here, the cell
                                    # should be occupied

                                    # continue doesn't do anything here because there's no code
                                    # after the if/else
                                    continue
                                else:
                                    # I think you're moving the agent to an occupied cell instead of
                                    # an unoccupied one
                                    nx = (x+j) % self.num_column
                                    ny = (y+i) % self.num_row
                                    if self.cells[ny][nx] == 0:
                                        self.cells[ny][nx] = column
                                        self.cells[y][x] = 0
                                        # the loop continues after moving, which causes multiple
                                        # moves, but the new y, x value will be 0 so nothing
                                        # happens; it is inefficient though
                                    else:
                                        # continue doesn't do anything here
                                        continue
                
            
        

    def run(self):
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(30) * 0.001

        pygame.quit()

game = Game()
game.run()