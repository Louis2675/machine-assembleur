import random
from parametres_terrain import P_PLAIN, P_FOREST, P_HOUSE, TERRAIN_SIZE, WATER_HEIGHT
from terrain import Terrain, Cell

def cell_generator(terrain):
    """
    Function to give each cell it's type between the three primary ones : Water, Forest or Plain
    Entry : terrain, wich we will change
    Sortie : the new terrain with each cell now having a type
    """
    for line in range (terrain.size):
        for col in range (terrain.size):
            # We take a number between 0 and 1
            alea = random.random()
            # We check if the number is under the probability for a forest
            if alea < P_FOREST:
                terrain.grid[line][col].terrain_type = 'F'
            # Same for a plain
            else:
                terrain.grid[line][col].terrain_type = 'P'
            
            # Now we check for the height of the cells and give the water type for the ones below the water height
            if terrain.grid[line][col].height <= WATER_HEIGHT:
                terrain.grid[line][col].terrain_type = 'W'
    return terrain



def generate_houses(terrain):
    """
    Function to place houses on the terrain

    Paramètres:
    terrain : l'objet terrain sur lequel on veut générer des maisons

    Retourne:
    terrain : le terrain avec les maisons générées
    """
    for line in range(terrain.size):  
        for col in range(terrain.size):
            random_number = random.random()
            if random_number < P_HOUSE and terrain.grid[line][col].terrain_type != "W":  # With a probability of P_HOUSE and if it is not water
                terrain.grid[line][col].terrain_type = 'H'  # The type is then a house
    return terrain


def new_height_randomizer(height):
    random_num = random.random()
    if random_num <= 0.5:
        if height != 0:
            height = height-1
    elif 0.5 < random_num :
        if height != 9:
            height = height + 1
    return height

def generate_heights(terrain):
    for line in range(terrain.size):
        for col in range(terrain.size):
            if col == line == 0:
                terrain.grid[line][col].height = random.randint(0,9)
            elif line == 0:
                new_height = new_height_randomizer(terrain.grid[line][col-1].height)
                terrain.grid[line][col].height = new_height
            elif col == 0 :
                new_height = new_height_randomizer(terrain.grid[line-1][col].height)
                terrain.grid[line][col].height = new_height
            else:
                height1 = new_height_randomizer(terrain.grid[line-1][col].height)
                height2 = new_height_randomizer(terrain.grid[line][col-1].height)

                terrain.grid[line][col].height = (height1 + height2) // 2
    return terrain

def change_cell (terrain, x, y):
    """
    Function that counts the number of each neighbour and give our cell the type of the most numerous neighbour
    """
    if x != 0 and col != 0 and line != terrain.size and col != terrain.size : # We make sur the cell is not bordering a side

def harmonization (terrain):
    for _ in range (10): # We do 10 turns of harminixing the terrain
        
        for line in range (terrain.size):
            for col in range (terrain.size):
                change_cell(terrain, line, col)


def generate_terrain ():
    terrain = Terrain(TERRAIN_SIZE)
    return generate_houses(cell_generator(generate_heights(terrain)))

if __name__ == "__main__":
    terrain = generate_terrain()
    terrain.display_grid()

