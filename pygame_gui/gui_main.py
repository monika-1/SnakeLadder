import pygame
from pygame_gui.board_drawer import BoardDrawer
from pygame_gui.game_controller import GameController

# Constants
WINDOW_SIZE_LENGTH = 600
WINDOW_SIZE_BREADTH = 700

# Game states
START_SCREEN = 0
GAME_RUNNING = 1

def draw_start_screen(screen, font, large_font):
    screen.fill((173, 216, 230))  # Light blue background

    # Draw game title
    title_surface = large_font.render("Snake and Ladder", True, (0, 0, 128))
    title_rect = title_surface.get_rect(center=(WINDOW_SIZE_LENGTH // 2, 100))
    screen.blit(title_surface, title_rect)

    # Load and display logo image or animation
    try:
        logo_image = pygame.image.load("assets/logo.png")
        logo_image = pygame.transform.scale(logo_image, (150, 150))
        screen.blit(logo_image, (WINDOW_SIZE_LENGTH // 2 - 75, 150))
    except:
        # Fallback animation: rotating square
        angle = pygame.time.get_ticks() // 10 % 360
        square = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(square, (255, 140, 0), (0, 0, 100, 100))
        rotated_square = pygame.transform.rotate(square, angle)
        rect = rotated_square.get_rect(center=(WINDOW_SIZE_LENGTH // 2, 225))
        screen.blit(rotated_square, rect)

    # Draw start button
    button_rect = pygame.Rect(WINDOW_SIZE_LENGTH // 2 - 100, 450, 200, 60)
    pygame.draw.rect(screen, (255, 255, 255), button_rect, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 2, border_radius=10)

    button_text = font.render("Start Game", True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE_LENGTH, WINDOW_SIZE_BREADTH))
    pygame.display.set_caption("Snake and Ladder")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)
    large_font = pygame.font.SysFont(None, 64)

    state = START_SCREEN
    board = BoardDrawer(screen)
    controller = GameController(board)

    running = True
    while running:
        screen.fill((255, 255, 255))

        if state == START_SCREEN:
            button_rect = draw_start_screen(screen, font, large_font)
        elif state == GAME_RUNNING:
            board.draw_board()
            controller.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if state == START_SCREEN and event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    state = GAME_RUNNING
            elif state == GAME_RUNNING:
                controller.handle_event(event)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
