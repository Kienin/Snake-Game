from tkinter import *
import random

# define constants:
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND = "black"


# define classes:

class Snake:
    # __init__(self): is a constructor
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            # makes snake appear in the top left corner
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            # makes the body of the snake
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE-1))  * SPACE_SIZE
        y = random.randint(0, (GAME_WIDTH/SPACE_SIZE-1))  * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill= FOOD_COLOR, tag="food")


# define functions:
def next_turn(snake, food):

    x, y = snake.coordinates[0]

    # the movement of the snake:
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR)
    snake.squares.insert(0, square)

    # score when snake coordinates are on food coordinates
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        # delete the last body part of the snake:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # game over is there's a collision
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    # defines the snake's movements:
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    # game over when snake collides with borders:
    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True

    # game over when snake collides with snake's body parts:
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part [1]:
            print("GAME OVER")
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('comic sans', 35), text="GAME OVER", fill= "red", tag="gameover")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=("comic sans", 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# to center when game pops up
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# bind keys:
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))

window.bind("<a>", lambda event: change_direction('left'))
window.bind("<d>", lambda event: change_direction('right'))
window.bind("<w>", lambda event: change_direction('up'))
window.bind("<s>", lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
