This project was created for an assignment of the 'File Organization' course.
# 9x9 Connect Four Game (Python)

This project is a **9x9 Connect Four-style game** written in Python. Two players take turns placing their tokens on the board, and the first player to align **4 tokens in a row** (horizontally, vertically, or diagonally) wins. All moves are also recorded in a file (`hamle.txt`).

---

## Features

- 9x9 game board
- Two-player turn-based gameplay (`X` and `O`)
- Moves are saved to a file (`hamle.txt`)
- Win detection (horizontal, vertical, diagonal)
- Simple console-based visual board

---

## Requirements

- Python 3.x

---

## How to Play

1. Download the project to your computer.
2. Open a terminal or command prompt.
3. Run the game file:

```bash
python game.py

Players take turns entering the column number (1-9) where they want to place their token.

The game ends when a player aligns 4 tokens in a row, and the winner is displayed.

All moves are recorded in hamle.txt.
1  2  3  4  5  6  7  8  9
                 
                 
                 
                 
                 
                 
                 
                 
                 
Player X's turn. Which column would you like to place your token (1-9)? 5
Files

game.py → The main game script

hamle.txt → Records all moves made by players
