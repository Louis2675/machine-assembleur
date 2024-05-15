import pygame
import generation_terrain
import propagation_incendie
import random
from parametres_terrain import TERRAIN_SIZE
from parametres_incendie import P_RAIN, T_RAIN, P_WIND, T_WIND

def calculate_rain(rain, time_rain):
    """
    Function to know if it is raining or not
    """
    nb_rand = random.random()
    if nb_rand <= P_RAIN and rain == False:
        rain = True
        time_rain = T_RAIN
    elif rain == True:
        if time_rain == 0:
            rain = False
        else :
            time_rain -= 1
    return rain, time_rain

def wind (direction, values, time):
    rand = random.random()
    if rand <= P_WIND and time == 0:
        nb_rand = random.randint(0,4)
        time = T_WIND
        return values[nb_rand], time
    elif time > 0 :
        return direction, time -1
    else :
        return direction, time

if __name__ == "__main__":
    # We start by initialising everything we need

    terrain = generation_terrain.generate_terrain()
    # initializing pygame
    pygame.font.init()

#    pygame.font.get_init()

    # Our main variables
    size = 800 # Hight of the screen, width is 1.3 times the height
    marge = size//10 # The size of the sides of our simulation
    size_grid = size - marge # The size of our 

    turn_count = 0 # The turn count for the simulation

    window = pygame.display.set_mode((size*1.3, size)) # Initialise the window

    running  = True # To start pygame

    color = (255,255,255) # Color of the backgrund

    rain = False
    time_rain = 0
    
    wind_values = ['n','l', 'u', 'r', 'd'] # the values are none, left, up, right, down
    wind_direction = wind_values[0]
    time_wind = 0

    """

    font1 = pygame.font.SysFont('freesanbold.ttf', 50)

    # The title for the sim
    text1 = font1.render('Welcome to the fire hazard simulator', True, (0, 0, 0))

    # create a rectangular object for the title
    textRect1 = text1.get_rect()

    # setting center for the title
    textRect1.center = (taille//2, 100)
    """

    # The colors for the different rectangles

    colorW = (21, 124, 214)
    colorP = (72, 232, 9)
    colorF = (44, 143, 6)
    colorH = (186, 123, 13)
    colorB = (232, 24, 9)
    colorC = (0,0,0)

    # Title of our window
    pygame.display.set_caption('Fire Hazard Sim')

    while running:
        
        """
        """
        turn_count = turn_count + 1

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT :  
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    x, y = event.pos
                    
                    if x > marge//2 and x < size_grid + marge//2 and y > marge//2 and y < size_grid + marge//2:
                        x, y = (x- marge //2)//(size_grid//TERRAIN_SIZE), (y - marge // 2)//(size_grid//TERRAIN_SIZE)
                        coors = (y, x)
                        propagation_incendie.set_fire(terrain, coors)
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        window.fill((255,255,255))

        #    The grid is displayed by looking at the cell's type and showing a particular color for this type of cell
        for line in range (terrain.size):
            for col in range (terrain.size):

                if terrain.grid[line][col].terrain_type == "C" :
                    pygame.draw.rect(window, colorC, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].burning == True:
                    pygame.draw.rect(window, (170 + (terrain.grid[line][col].fire_strength * 9), 10+ (terrain.grid[line][col].fire_strength * 10), 10+ (terrain.grid[line][col].fire_strength * 10)), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'F':
                    pygame.draw.rect(window, colorF, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'W':
                    pygame.draw.rect(window, colorW, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'P':
                    pygame.draw.rect(window, colorP, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'H':
                    pygame.draw.rect(window, colorH, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))



        pygame.display.flip() # To refresh the screen

        pygame.time.wait(100) # We wait a bit until the next step

        rain, time_rain = calculate_rain(rain, time_rain)

        wind_direction, time_wind = wind(wind_values)

        propagation_incendie.simulation_step(terrain, turn_count, rain, wind_direction)

