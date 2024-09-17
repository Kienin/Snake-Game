# 🐍  Snake Game in Python with Tkinter
This is a simple implementation of the classic Snake game using Python and the Tkinter library for graphical interface. The game consists of a snake that moves around the screen, eating food and growing longer. The game ends if the snake collides with the borders of the window or itself.

## Features
- Basic Gameplay: Control the snake to eat the food and grow longer.
- Collision Detection: End the game if the snake hits the borders or itself.
- Score Tracking: Display the current score on the screen.
- Controls: Use arrow keys or WASD keys to change the direction of the snake.

## Requirements
1. Python 3.x
2. Tkinter library (comes with standard Python installations)

## How to Run
- Install Python: Ensure you have Python 3.x installed on your machine. You can download it from python.org.

- Save the Code: Copy the code provided into a file named snake_game.py.

- Run the Game: Open a terminal or command prompt, navigate to the directory where snake_game.py is saved, and run the following command:

- Play the Game: Use the arrow keys or WASD keys to control the direction of the snake. Try to eat the red food to increase your score and avoid collisions to prevent the game from ending.

## Code Breakdown

### Constants:

  - GAME_WIDTH and GAME_HEIGHT: Dimensions of the game window.
  
  - SPEED: Speed at which the game updates.
  
  - SPACE_SIZE: Size of each square (snake body part and food).
  
  - BODY_PARTS: Initial length of the snake.
  
  - SNAKE_COLOR and FOOD_COLOR: Colors for the snake and food.
  
  - BACKGROUND: Background color of the canvas.

### Classes:

  🐍 Snake: Handles the creation and management of the snake, including its movement and growth.
  
  🍎 Food: Randomly generates food in the game area.

### Functions:

  - next_turn(snake, food): Updates the game state, moves the snake, checks for collisions, and handles food consumption.
  
  - change_direction(new_direction): Changes the direction of the snake based on user input.
  
  - check_collisions(snake): Checks if the snake has collided with the borders or itself.
  
  - game_over(): Displays the game over message and clears the canvas.

### Game Initialization:

  - Sets up the game window, score label, canvas, and binds keyboard events to control the snake.
  
  - Starts the game loop with next_turn(snake, food) and enters the Tkinter main event loop

## Credits
🎓 Credits - @BroCode on Youtube (https://youtu.be/bfRwxS5d0SI?si=BQDzwDa6B4dPkrFF)
