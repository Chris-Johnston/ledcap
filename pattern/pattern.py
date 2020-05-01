"""
Pattern base class
"""

from abc import ABC, abstractmethod

class Pattern(ABC):
    def __init__(self, colors: list, dimensions: tuple):
        self.colors = colors
        self.dimensions = dimensions

    @abstractmethod
    def update(self):
        pass

    def coords_to_index(self, coords: tuple) -> int:
        return len(self.colors) * coords[1] + coords[0]

    def index_to_coords(self, index: int) -> tuple:
        return (int(index / len(self.colors)), index % len(self.colors))

    def __max_index__(self):
        return self.dimensions[0] * self.dimensions[1]

    def __iter__(self):
        """
        iterates a tuple with idx and color value
        """
        for idx in range(self.__max_index__()):
            yield (idx, self.__getitem__(idx))
    
    def __getitem__(self, key):
        assert 0 <= key < self.__max_index__()
        coords = self.index_to_coords(key)
        print(f"index {key} [{coords[0]}, {coords[1]}]")
        return self.colors[coords[0]][coords[1]]

    def __setitem__(self, key, value):
        assert 0 <= key < self.__max_index__()
        assert 0 <= value <= 0xffffff
        x, y = self.index_to_coords(key)
        self.colors[x][y] = value


