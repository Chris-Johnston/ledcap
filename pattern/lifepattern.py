"""
Game of Life Pattern

Game of life. Every Xs, a new random pixel is turned on to ensure
that it doesn't get stuck.

Updates at 10hz
"""

from pattern.pattern import Pattern
import itertools
import random
import time

class LifePattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        # init 2d array of cells
        self.cells = []
        for _ in range(dimensions[0]):
            new = [False for _ in range(dimensions[1])]
            self.cells.append(new)
        # turn on 5 px
        for _ in range(25):
            self.randomly_set()

    def process_life(self):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                state = self.cells[x][y]
                neighbors = self.get_num_neighbors(x, y)
                self.cells[x][y] = self.get_live_or_die(state, neighbors)
                
    def get_live_or_die(self, current_state: bool, num_neighbors: int) -> bool:
        if current_state and num_neighbors < 2:
            return False
        if current_state and 2 <= num_neighbors <= 3:
            return True
        if current_state and num_neighbors > 3:
            return False
        if not current_state and num_neighbors == 3:
            return True
        # else, use the same state
        return current_state

    def get_num_neighbors(self, x: int, y: int) -> int:
        return sum(self.get_neighbor_states(x, y))

    def get_neighbor_states(self, x, y):
        for neighbor in self.get_neighbors(x, y):
            yield self.cells[neighbor[0]][neighbor[1]]
        
    def get_neighbors(self, x: int, y: int):
        combinations = [
            [x - 1, x, x + 1],
            [y - 1, y, y + 1]
        ]
        for coord in itertools.product(*combinations):
            if coord == (x, y):
                continue
            if coord[0] < 0 or coord[0] >= self.dimensions[0]:
                continue
            if coord[1] < 0 or coord[1] >= self.dimensions[1]:
                continue
            yield coord
    
    def randomly_set(self):
        """
        Randomly enables a cell, even if on already
        """
        x = random.randint(0, self.dimensions[0] - 1)
        y = random.randint(0, self.dimensions[1] - 1)
        self.cells[x][y] = True

    def update(self):
        time.sleep(0.2)        
        for _ in range(5):
            self.randomly_set()
        self.process_life()
        for idx, _ in self:
            coords = self.index_to_coords(idx)
            if self.cells[coords[0]][coords[1]]:
                self[idx] = 0x00ff00
            else:
                self[idx] = 0x0

