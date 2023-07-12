import time
from tkinter import *
import random

SPACE_SIZE = 50
BODY_SIZE = 3
SPEED = 150

class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_SIZE):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill = "#0000ff", tag="snake")
            self.squares.append(square)
class Food:

    def __init__(self):

        x = random.randint(0, (700/SPACE_SIZE) -1) * SPACE_SIZE
        y = random.randint(0, (700 / SPACE_SIZE) -1) * SPACE_SIZE

        self.cooridnates = [x,y]

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill="#ff7f24", tag="food")

def next_move(snake,food):

    x, y = snake.coordinates[0]

    if direction == "up":
       y-= SPACE_SIZE
    elif direction == "down":
       y += SPACE_SIZE
    elif direction == "right":
       x += SPACE_SIZE
    elif direction == "left":
       x -= SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill="#0000ff")

    snake.squares.insert(0,square)

    if x == food.cooridnates[0] and y == food.cooridnates[1]:
        global score
        score += 1
        score_board.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_move, snake, food)

def change_direction(new_direction):

    global direction

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
def check_collision(snake):

    x, y = snake.coordinates[0]

    if x<0 or x>= 700:
        return True
    elif x<0 or x>= 700:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

        return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(700/2, 500/2, font="consolas 40 bold", text="GAME OVER", fill="red")


#I'm starting to build the window
window = Tk()
window.title('SNAKE GAME')
window.resizable(False, False)

score = 0
direction = "down"


def start_game():
    frame.destroy()
    open_button.destroy()
    # I set the color and size of the background
    global canvas
    canvas = Canvas(window, height=700, width=700, bg="#000000")
    canvas.pack()

    snake = Snake()
    food = Food()
    next_move(snake, food)



frame = Label(width = 700, height = 700)
frame.pack()

open_button = Button(frame, font="consolas 40 bold", text="START", command=lambda: start_game())
open_button.pack()

#I am preparing the font and background of the score table
score = 0
score_board = Label(window,bg="white", text = "SCORE:{}".format(score), font = "consolas 40 bold",)
score_board.pack()




#I make the pop-up window appear in the middle of the screen.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"700x700+{(screen_width//2)-350}+{(screen_height//2)-350}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))



window.mainloop()