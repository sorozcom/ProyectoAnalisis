import pygame

#--- GLOBAL CONSTANTS ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH  = 700
SCREEN_HEIGHT = 500

class Game(object):
    """ This class represents a game instance. if restart the game is needed only 
        is require to create other instance of this class."""
 
    def __init__(self):
        """ Constructor. Initialize the game Instance"""
 
    def event_processor(self):
        """Detects the events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
 
    def execution_logic(self):
        """Executes the differents functions of the game"""

    def display_frame(self, window):
        """Draw each frame of the game"""
        window.fill(WHITE)
        pygame.display.flip()