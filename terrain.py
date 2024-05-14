"""
Fichier contenant la classe grid définissant une grid de jeu.
"""

class Cell:
    def __init__(self, terrain_type, fire_strength, height, x, y):
        self.terrain_type = terrain_type # For each of the type of terrains
        self.fire_strength = fire_strength # The fire strength that calculates the probability to propagate to a neighbour cell
        self.height = height # Inutile
        self.coors = (x, y) # The cells coordinates
        self.burning = False # Is the cell burning
        self.dying = False # Is the fire dying


class Terrain:
    def __init__ (self, size):
        self.size = size
        self.grid = []
        for line in range (size):
            self.grid.append([])
            for col in range (size) : 
                self.grid[line].append(Cell("None", 0, 0, line, col))

    
    # Inutile
    def display_grid(self):
        for line in range(self.size):
            print()
            for col in range(self.size):
                if self.grid[line][col].height <= 0:
                    print("\033[1;36m{}\033[1;37m".format(self.grid[line][col].height), end="")
                else:
                    print("\033[1;32m{}\033[1;37m".format(self.grid[line][col].height), end="")
