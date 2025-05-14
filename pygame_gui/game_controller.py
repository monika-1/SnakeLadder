# pygame_gui/game_controller.py

import pygame
import random
from game.board import snakes, ladders  # Importing from boards.py

# Function to generate a random color avoiding green and other forbidden colors
def get_random_player_color(forbidden_colors):
    while True:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if color not in forbidden_colors:
            return color

# Function to generate a random player color from a predefined list
# def get_random_player_color(available_colors):
#     return random.choice(available_colors)

class GameController:
    def __init__(self, board):
        self.board = board

        # List of acceptable colors (excluding green)
        self.forbidden_colors = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 0), (255, 218, 185), (255, 255, 153), (204, 255, 204)]

        self.players = [
            {'pos': 1, 'name': 'Player 1', 'color': get_random_player_color(self.forbidden_colors), 'shape': 'rect'},
            {'pos': 1, 'name': 'Player 2', 'color': get_random_player_color(self.forbidden_colors), 'shape': 'triangle'}
        ]
        self.current_player = 0
        self.font = pygame.font.SysFont(None, 32)
        self.dice_result = None
        self.winner = None  # Track winner

    def update(self):
        self.draw_players()
        self.draw_dice()
        self.draw_player_info()  # Display current player's info
        if self.winner:
            self.show_winner_popup()

    def show_winner_popup(self):
        # Create semi-transparent overlay (popup background)
        popup_surface = pygame.Surface((400, 200), pygame.SRCALPHA)
        popup_surface.fill((0, 0, 0, 180))  # Semi-transparent background

        # Winner text
        winner_text = f"{self.winner} WINS!"
        winner_surface = self.font.render(winner_text, True, (255, 255, 255))
        popup_surface.blit(winner_surface, (120, 50))  # Position winner message

        # Restart text
        restart_text = "Press R to Restart"
        restart_surface = self.font.render(restart_text, True, (255, 255, 255))
        popup_surface.blit(restart_surface, (120, 150))  # Position restart message

        # Blit the popup on top of the board screen (centered on screen)
        popup_x = (self.board.screen.get_width() - popup_surface.get_width()) // 2
        popup_y = (self.board.screen.get_height() - popup_surface.get_height()) // 2
        self.board.screen.blit(popup_surface, (popup_x, popup_y))

    def draw_players(self):
        for idx, player in enumerate(self.players):
            row, col = divmod(player['pos'] - 1, 10)
            if row % 2 == 1:
                col = 9 - col
            x = col * 60 + 30
            y = (9 - row) * 60 + 30

            color = player['color']
            shape = player['shape']

            if shape == 'rect':
                pygame.draw.rect(self.board.screen, color, pygame.Rect(x - 15, y - 15, 30, 30))
            elif shape == 'triangle':
                points = [(x, y - 18), (x - 15, y + 15), (x + 15, y + 15)]
                pygame.draw.polygon(self.board.screen, color, points)
                
    def draw_dice(self):
        # Display dice result
        dice_text = f"Dice: {self.dice_result}" if self.dice_result else "Press SPACE to roll"
        dice_surface = self.font.render(dice_text, True, (0, 0, 0))
        self.board.screen.blit(dice_surface, (10, self.board.screen.get_height() - 80))

        # Display current player's turn (below the dice)
        current_turn_text = f"Turn: {self.players[self.current_player]['name']}"
        current_turn_surface = self.font.render(current_turn_text, True, (0, 0, 0))
        self.board.screen.blit(current_turn_surface, (10, self.board.screen.get_height() - 30))  # Position below dice

    def draw_player_info(self):
        # Display player info mapping on the right side
        for idx, player in enumerate(self.players):
            symbol_text = f"{player['name']}:"
            symbol_surface = self.font.render(symbol_text, True, (0, 0, 0))
            self.board.screen.blit(symbol_surface, (self.board.screen.get_width() - 250, self.board.screen.get_height() - (80-50*idx)))  # Position for each player

            # Draw the player's symbol next to their name
            shape = player['shape']
            x_offset = self.board.screen.get_width() - 140  # Adjust as needed for spacing
            y_offset = self.board.screen.get_height() - (80 - 50*idx)
            if shape == 'rect':
                pygame.draw.rect(self.board.screen, player['color'], pygame.Rect(x_offset, y_offset, 20, 20))
            elif shape == 'triangle':
                points = [(x_offset + 10, y_offset), (x_offset, y_offset + 20), (x_offset + 20, y_offset + 20)]
                pygame.draw.polygon(self.board.screen, player['color'], points)

    def handle_event(self, event):
        if self.winner:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset_game()
            return

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.dice_result = random.randint(1, 6)
            player = self.players[self.current_player]
            player['pos'] += self.dice_result
            if player['pos'] > 100:
                player['pos'] = 100

            player['pos'] = self.snake_or_ladder(player['pos'])

            if player['pos'] == 100:
                self.winner = f"{player['name']}"
                return

            self.current_player = (self.current_player + 1) % len(self.players)

    def reset_game(self):
        # Reset player positions
        for player in self.players:
            player['pos'] = 1
        
        for player in self.players:
            player['color'] = get_random_player_color(self.forbidden_colors)  # Assign a new color

        self.current_player = 0
        self.dice_result = None
        self.winner = None

    def snake_or_ladder(self, pos):
        if pos in snakes:
            pos = snakes[pos]
        elif pos in ladders:
            pos = ladders[pos]
        return pos
