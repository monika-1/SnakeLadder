
# 🎲 Snake and Ladder Game

A Python implementation of the classic **Snake and Ladder** game, featuring:

- A **Command-Line Interface (CLI)** version
- A **Graphical User Interface (GUI)** version built with `pygame`

---

## 📋 Features

- 🎮 Supports 2 to 4 players
- 🐍 Snakes and 🪜 ladders based on standard positions
- 🎲 Random dice roll between 1–6
- 🏁 Win condition: land **exactly** on square 100
- ⌛ Turn-based gameplay
- ✅ Modular codebase (easily extendable)

---

## 📁 Project Structure

```
SnakeLadder/
│
├── main.py                 # Entry point for the CLI game
├── README.md               # Project documentation
│
├── game/                   # Game logic components
│   ├── __init__.py
│   ├── board.py            # Snake and ladder positions
│   ├── dice.py             # Dice rolling logic
│   ├── engine.py           # Game loop and interaction
│   └── player.py           # Player class and movement
│
├── pygame_gui/
│   ├── assets/
│   │  ├── background.mp3
│   │  ├── congratulations_music.mp3
│   │  ├── dice_roll.mp3
│   │  ├── ladder_climb.mp3
│   │  ├── logo.png
│   │  └── snake_bite.mp3
│   ├── __init__.py
│   ├── board_drawer.py
│   ├── game_controller.py
│   └── gui_main.py
|
└── tests/                  # Placeholder for future unit tests
    ├── __init__.py
    └── test_game.py
```

---

## 🚀 Getting Started

### 1. ✅ Prerequisites

- Python 3.6 or higher

### 2. ⬇️ Clone the Repository

```bash
git clone https://github.com/monika-1/SnakeLadder.git
cd SnakeLadder
```
---

## 🚀 How to Run the Game

### 🔹 CLI Version

To play the game in the terminal:

1. Open a terminal window.
2. Navigate to the `cli_version` directory.
3. Run the game using:

```bash
python3 main.py
```
---

### 🔸 GUI Version

To play the game with a graphical board using `pygame`:

1. Create a virtual environment:

```bash
python3 -m venv myenv
```

2. Activate the virtual environment:

- On macOS/Linux:

```bash
source myenv/bin/activate
```

- On Windows (if needed):

```bash
myenv\Scripts\activate
```

3. Install `pygame`:

```bash
pip install pygame
```

4. Run the game:

```bash
python3 -m pygame_gui.gui_main
```

5. When you're done, deactivate the virtual environment:

```bash
deactivate
```
---

## 🧑‍💻 Gameplay Instructions

1. Each player takes turns to roll the dice.
2. If you land on:
   - 🐍 Snake: You move **down** to the tail.
   - 🪜 Ladder: You move **up** to the top.
3. You must roll the exact number to reach square 100 and win.
4. First player to reach 100 wins! 🏆

---

## 🛠 How It Works
### 🔹 CLI Version
- `board.py`: Contains the snake and ladder positions using dictionaries.
- `dice.py`: Simulates a dice roll using `random.randint(1, 6)`.
- `player.py`: Defines the `Player` class and handles movement and state.
- `engine.py`: Manages the game loop, player turns, win condition.
- `main.py`: Starts the CLI game by invoking the engine.

### 🔸 GUI Version
- `board_drawer.py`: Responsible for visually rendering the Snake and Ladder board layout in the GUI version using `pygame`.
- `game_controller.py`: Handles the core game logic, including player turns, dice rolls, and movement across the Snake and Ladder board.
- `gui_main.py`: Launches the GUI for the Snake and Ladder game using Pygame, managing the visual board, player interactions, and game events.

---

## ✅ Features

- 🎲 Dice roll simulation
- 🐍 Snake and ladder positions
- 👥 Two-player support
- 🏁 Win condition at position 100
- 🖼️ GUI version with visual board and player movement

---

## ✅ Future Improvements

- 🌐 Web version using Flask or Django
- 💾 Save/Load game progress
- 📈 Player statistics and leaderboard
- 🔁 Rematch/restart options

---

## 📦 Requirements

- **CLI version**: No external dependencies.
- **GUI version**: Requires `pygame`.

To install dependencies for the GUI version:

```bash
pip install pygame
```

---

## 🧪 Testing (Coming Soon)

```bash
cd tests
pytest test_game.py
```

*Note: Add your test cases in `test_game.py`.*

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 👩‍💻 Author

**Monika Kumari**  
GitHub: [@monika-1](https://github.com/monika-1)  
Email: monikakumari33@gmail.com

---

## 🙌 Acknowledgements

- Classic board game concept: *Snakes and Ladders*
- Python documentation
- ASCII Art and Emojis for better UX 🎉
