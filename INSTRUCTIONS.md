# Rochambeau Game Instructions

## Text-Based Game (rochambeau.py)

1. **Start the Game**
   - Run: `python rochambeau.py`

2. **Making a Move**
   - Enter your choice as:
     - Full word: `rock`, `paper`, or `scissors`
     - Single letter: `r`, `p`, or `s` (case-insensitive)
     - Number: `1` (rock), `2` (paper), `3` (scissors)

3. **Game Flow**
   - The computer randomly selects its move.
   - Both choices are displayed (with ASCII art and side-by-side animation).
   - The winner is announced and the scoreboard updates.
   - To exit, enter `4`, `e`, `q`, `x`, or `exit` at any prompt.

4. **Scoreboard**
   - Tracks your wins, computer wins, and ties.
   - Shown at the top of each round.

---

## GUI Game (rochambeau_gui.py)

1. **Setup**
   - Install PySide6: `pip install PySide6`
   - Place `rock.png`, `paper.png`, and `scissors.png` in an `images/` folder in the project directory.


2. **Start the Game**
   - Run: `python rochambeau_gui.py`

3. **Playing**
   - Click the Rock, Paper, or Scissors button (with icons) to make your move.
   - The computer will play against you instantly.
   - Your choice and the computer's choice are shown with images and labels.
   - The result and updated score are displayed after each round.
   - Click Exit to quit the game.

4. **Modern Features**
   - Stylish scoreboard and buttons
   - Responsive layout and color highlights
   - PNG icons for a modern look

---

### Creating a Standalone Executable (Windows)

You can build a standalone `.exe` for the GUI game using PyInstaller. The code now ensures images are bundled and display correctly in the executable.

1. Install PyInstaller (if not already):
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   pyinstaller --noconfirm --onefile --windowed --add-data "images;images" rochambeau_gui.py
   ```
3. The `.exe` will be in the `dist` folder. Double-click to run. No Python installation is needed for end users.

**Note:** The game uses a `resource_path` helper to ensure images work in both script and executable modes.

---

## Tips
- You can play as many rounds as you like in either version.
- The GUI version is more visually appealing and user-friendly.
- The text version is great for quick play in a terminal or for scripting/testing.

Enjoy Rochambeau!
