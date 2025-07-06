# Rochambeau (Rock-Paper-Scissors)

A fun, modern version of the classic game Rock-Paper-Scissors (Rochambeau) in Python. Includes both a text-based terminal game and a beautiful PySide6 GUI version.

## Features
- Play in the terminal or with a modern graphical interface
- Animated ASCII art (text version) or real images (GUI version)
- Flexible input: full word, single letter, or number (text version)
- Scoreboard and round tracking
- Stylish, responsive GUI with icons and gradients
- Automated tests for quality assurance

## How to Play

### Text Version
1. Run the script:
   ```
   python rochambeau.py
   ```
2. Enter your move as a word (rock, paper, scissors), a letter (r, p, s), or a number (1, 2, 3).
3. The computer will play against you, and the winner is shown after each round.
4. The scoreboard updates after every round. Enter 4, e, q, x, or exit to quit.

### GUI Version
1. Make sure you have PySide6 installed:
   ```
   pip install PySide6
   ```
2. Place your PNG images for rock, paper, and scissors in an `images/` folder.
3. Run the GUI:
   ```
   python rochambeau_gui.py
   ```
4. Click the Rock, Paper, or Scissors buttons to play. The GUI will show your choice, the computer's choice, and update the score.
5. Click Exit to quit.

#### Building a Standalone Executable (Windows)
You can create a standalone `.exe` for the GUI version using PyInstaller. Images are now bundled automatically and will display correctly in the executable.

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   pyinstaller --noconfirm --onefile --windowed --add-data "images;images" rochambeau_gui.py
   ```
3. The `.exe` will be in the `dist` folder. Double-click to run. No Python installation is needed for end users.

**Note:** The code uses a `resource_path` helper to ensure images load correctly in both script and executable modes.

## Automated Testing
- Run all tests with:
  ```
  python -m unittest discover
  ```
- See `test_game_flow.py` for simulated user interaction tests.

## Requirements
- Python 3.x
- PySide6 (for GUI)

## Project Structure
```
Rochambeau/
├── rochambeau.py           # Text-based game
├── rochambeau_gui.py       # GUI game (PySide6)
├── images/                 # PNG images for GUI
│   ├── rock.png
│   ├── paper.png
│   └── scissors.png
├── test_game_flow.py       # Automated tests
├── README.md               # Project overview
├── INSTRUCTIONS.md         # Detailed instructions
└── ...
```

## Enjoy the game!
Feel free to modify or extend the game with new features, such as multiplayer mode, statistics, or more hand gestures!
