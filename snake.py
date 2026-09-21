import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
SIZE = 20

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#001ADE"
)

canvas.pack()

snake = []
direction = "Right"
food = []
game_running = True


def restart_game():
    global snake, direction, food, game_running

    snake = [
        [300, 200],
        [280, 200],
        [260, 200]
    ]

    direction = "Right"

    food = [
        random.randrange(0, WIDTH, SIZE),
        random.randrange(0, HEIGHT, SIZE)
    ]

    game_running = True

    draw()
    game()


def change_direction(event):
    global direction

    if event.keysym == "Up" and direction != "Down":
        direction = "Up"

    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"

    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"

    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"


def game():
    global food, game_running

    if not game_running:
        return

    head = snake[0].copy()

    if direction == "Up":
        head[1] -= SIZE

    elif direction == "Down":
        head[1] += SIZE

    elif direction == "Left":
        head[0] -= SIZE

    elif direction == "Right":
        head[0] += SIZE

    if (
        head[0] < 0 or
        head[0] >= WIDTH or
        head[1] < 0 or
        head[1] >= HEIGHT or
        head in snake
    ):
        game_over()
        return

    snake.insert(0, head)

    if head == food:
        food = [
            random.randrange(0, WIDTH, SIZE),
            random.randrange(0, HEIGHT, SIZE)
        ]
    else:
        snake.pop()

    draw()

    root.after(300, game)


def draw():
    canvas.delete("all")

    for i, part in enumerate(snake):

        color = "lime" if i == 0 else "green"

        canvas.create_oval(
            part[0],
            part[1],
            part[0] + SIZE,
            part[1] + SIZE,
            fill=color
        )

    canvas.create_oval(
        food[0],
        food[1],
        food[0] + SIZE,
        food[1] + SIZE,
        fill="red"
    )


def game_over():
    global game_running

    game_running = False

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="GAME OVER",
        fill="white",
        font=("Arial", 30)
    )


restart_button = tk.Button(
    root,
    text="RESTART GAME",
    command=restart_game
)

restart_button.pack(pady=10)

root.bind("<KeyPress>", change_direction)

restart_game()

root.mainloop()
