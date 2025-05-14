import pygame
from game.board import snakes, ladders  # Importing snakes and ladders from board.py

class BoardDrawer:
    def __init__(self, screen):
        self.screen = screen
        self.grid_size = 10
        self.cell_size = 60
        self.snakes = snakes  # Using snakes from board.py
        self.ladders = ladders  # Using ladders from board.py
        self.font = pygame.font.SysFont(None, 24)  # Font for text rendering

    def draw_board(self):
        # Draw the board starting from the top of the screen
        number = 1
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Zig-zag numbering: alternate row direction
                display_col = col if row % 2 == 0 else (self.grid_size - 1 - col)
                x = display_col * self.cell_size
                y = (self.grid_size - 1 - row) * self.cell_size  # Start from the top

                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

                # Alternate based on cell number
                color = (255, 255, 153) if number % 2 == 1 else (204, 255, 204)  # Yellow for odd, Green for even

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Black border

                # Render the number
                text = self.font.render(str(number), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)

                number += 1

        # Draw Snakes
        self.draw_snakes()

        # Draw Ladders
        self.draw_ladders()

        # Draw the footer (this should be called after drawing the board)
        self.draw_footer()

    def draw_footer(self):
        # Background for footer, drawing it at the bottom of the screen with grey color
        footer_rect = pygame.Rect(0, self.screen.get_height() - 2*(self.cell_size-10), self.screen.get_width(), 2*(self.cell_size-10))
        pygame.draw.rect(self.screen, (255, 218, 185), footer_rect)  # Grey color

    def draw_snakes(self):
        for start, end in self.snakes.items():
            start_row, start_col = divmod(start - 1, 10)
            end_row, end_col = divmod(end - 1, 10)
            
            start_x = start_col * self.cell_size + self.cell_size // 2
            start_y = (9 - start_row) * self.cell_size + self.cell_size // 2  # No header adjustment here
            end_x = end_col * self.cell_size + self.cell_size // 2
            end_y = (9 - end_row) * self.cell_size + self.cell_size // 2  # No header adjustment here
            
            # Draw the snake body as a curved line (optional: use a zigzag)
            pygame.draw.line(self.screen, (255, 0, 0), (start_x, start_y), (end_x, end_y), 5)
            
            # Snake head (start point)
            pygame.draw.circle(self.screen, (255, 0, 0), (start_x, start_y), 10)

    def draw_ladders(self):
        for start, end in self.ladders.items():
            start_row, start_col = divmod(start - 1, 10)
            end_row, end_col = divmod(end - 1, 10)
            
            start_x = start_col * self.cell_size + self.cell_size // 2
            start_y = (9 - start_row) * self.cell_size + self.cell_size // 2  # No header adjustment here
            end_x = end_col * self.cell_size + self.cell_size // 2
            end_y = (9 - end_row) * self.cell_size + self.cell_size // 2  # No header adjustment here
            
            # Offset for ladder side rails
            offset = 10
            pygame.draw.line(self.screen, (0, 255, 0), (start_x - offset, start_y), (end_x - offset, end_y), 3)
            pygame.draw.line(self.screen, (0, 255, 0), (start_x + offset, start_y), (end_x + offset, end_y), 3)
            
            # Draw rungs
            num_rungs = 5
            for i in range(num_rungs + 1):
                rung_x1 = start_x - offset + (end_x - start_x) * i / num_rungs
                rung_y1 = start_y + (end_y - start_y) * i / num_rungs
                rung_x2 = start_x + offset + (end_x - start_x) * i / num_rungs
                rung_y2 = start_y + (end_y - start_y) * i / num_rungs
                pygame.draw.line(self.screen, (0, 255, 0), (rung_x1, rung_y1), (rung_x2, rung_y2), 2)
