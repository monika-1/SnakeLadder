
# 🎲 Snake and Ladder CLI Game in Python

A modular, command-line implementation of the classic **Snake and Ladder** board game for 2 to 4 players. Built in Python, this version emphasizes clean code architecture and expandability for future GUI or web-based implementations.

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
├── main.py                 # Entry point for the game
├── README.md               # Project documentation
│
├── game/                   # Game logic components
│   ├── __init__.py
│   ├── board.py            # Snake and ladder positions
│   ├── dice.py             # Dice rolling logic
│   ├── engine.py           # Game loop and interaction
│   └── player.py           # Player class and movement
│
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

### 3. ▶️ Run the Game

```bash
python3 main.py
```

---

## 🧑‍💻 Gameplay Instructions

1. Run the game with `python main.py`.
2. Type `start` to begin the game.
3. Enter the number of players (between 2 and 4).
4. Each player takes turns to roll the dice.
5. If you land on:
   - 🐍 Snake: You move **down** to the tail.
   - 🪜 Ladder: You move **up** to the top.
6. You must roll the exact number to reach square 100 and win.
7. First player to reach 100 wins! 🏆

---

## 🛠 How It Works

- `board.py`: Contains the snake and ladder positions using dictionaries.
- `dice.py`: Simulates a dice roll using `random.randint(1, 6)`.
- `player.py`: Defines the `Player` class and handles movement and state.
- `engine.py`: Manages the game loop, player turns, win condition.
- `main.py`: Starts the game by invoking the engine.

---

## ✅ Future Improvements

- 🎨 GUI using `tkinter` or `pygame`
- 🌐 Web version using Flask or Django
- 💾 Save/Load game progress
- 📈 Player statistics and leaderboard
- 🔁 Rematch/restart options

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
