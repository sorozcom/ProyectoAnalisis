import pygame
from game import Game, SCREEN_HEIGHT, SCREEN_WIDTH
def main():
    """Main function of the game"""
    # Pygame Initialization
    pygame.init()  
    dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
    window = pygame.display.set_mode(dimensions)
    pygame.display.set_caption("Piratas por el Mundo")
    pygame.mouse.set_visible(False)
    close = False
    time = pygame.time.Clock()
    # A game Object
    game = Game()
    # Main Loop
    while not close:        
        # Event processor
        close = game.event_processor()
        # Game Logic
        game.execution_logic()
        # Draw current frame
        game.display_frame(window)
        # Frame per Second
        time.tick(60)
    # Close the window an finish the game
    pygame.quit()
# Call the main function and start the game
if __name__ == "__main__":
    main()