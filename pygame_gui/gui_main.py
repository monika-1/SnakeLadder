# pygame_gui/gui_main.py

import pygame
from pygame_gui.board_drawer import BoardDrawer
from pygame_gui.game_controller import GameController

# Constants
WINDOW_SIZE_LENGTH = 600
WINDOW_SIZE_BREADTH = 700

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE_LENGTH, WINDOW_SIZE_BREADTH))
    pygame.display.set_caption("Snake and Ladder")

    clock = pygame.time.Clock()
    board = BoardDrawer(screen)
    controller = GameController(board)

    running = True
    while running:
        screen.fill((255, 255, 255))
        board.draw_board()
        controller.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            controller.handle_event(event)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
