import random
from random import randint
import tkinter as tk
WIDTH = 300
HEIGHT = 200
simbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

class Ball:
    def __init__(self):
        self.R = randint(10, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R,
                                     fill= '#' + random.choice(simbols)+random.choice(simbols)+random.choice(simbols)+random.choice(simbols)+random.choice(simbols)+random.choice(simbols))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def ballsmaker(*args):
    balls.append(Ball())
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

root = tk.Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = tk.Canvas(root)
canvas.pack()

canvas.bind('<Button-1>', ballsmaker)
balls = []
tick()
root.mainloop()
