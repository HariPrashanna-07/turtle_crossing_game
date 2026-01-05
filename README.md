# Turtle Crossing Game

A classic arcade-style game built with Python's Turtle module. Help the turtle cross the busy road without getting hit by the cars!

## How to Play

The player controls a turtle that starts at the bottom of the screen. The goal is to reach the top edge of the screen.

### Controls
- **Up Arrow**: Move the turtle forward.

### Rules
- Avoid the cars moving across the screen.
- If the turtle collides with a car, it's GAME OVER.
- Upon reaching the top, the player levels up:
  - The turtle returns to the starting position.
  - The car speed increases for the next level.

## Requirements

- Python 3.x
- `turtle` module (included in Python standard library)

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the game:

   ```bash
   python main.py
   ```

## Files Description

- `main.py`: The entry point of the game. Handles the game loop and screen setup.
- `player.py`: Contains the `Player` class, defining the turtle's movement and behavior.
- `car_manager.py`: Contains the `CarManager` class, responsible for generating and moving cars.
- `scoreboard.py`: Contains the `Scoreboard` class, which tracks the current level and displays "Game Over".
