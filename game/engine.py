from .board import snakes, ladders
from .player import Player
from .dice import roll

def start_game():
    print("🎲 Welcome to the Snake and Ladder Game 🎲")
    
    while True:
        start_input = input("Type 'start' to begin the game: ").strip().lower()
        if start_input == 'start':
            break
        print("Invalid input. Please type 'start'.")

    while True:
        try:
            count = int(input("Enter number of players (2–4): "))
            if 2 <= count <= 4:
                break
            print("Enter a number between 2 and 4.")
        except ValueError:
            print("Invalid number.")

    players = [Player(f"Player {i+1}") for i in range(count)]
    winner = None

    while not winner:
        for player in players:
            input(f"{player.name}'s turn. Press Enter to roll the dice...")
            dice = roll()
            print(f"{player.name} rolled a {dice}")

            old_position = player.position
            player.move(dice)

            if player.position in snakes:
                print(f"Oh no! {player.name} got bitten by a snake 🐍 and goes to {snakes[player.position]}")
                player.position = snakes[player.position]
            elif player.position in ladders:
                print(f"Yay! {player.name} climbed a ladder 🪜 to {ladders[player.position]}")
                player.position = ladders[player.position]

            print(f"{player.name} moved from {old_position} to {player.position}")
            print("-" * 40)

            if player.position == 100:
                winner = player.name
                break

    print(f"\n🏆 {winner} wins the game! Congratulations! 🏆")
