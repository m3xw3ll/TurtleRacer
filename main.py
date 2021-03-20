from turtle import *
import turtle
from random import randrange
import tkinter
import tkinter as tk

WIDTH = 600
HEIGHT = 600
TURTLE_SIZE = 10
BOTS = 6

class Racer():
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.runner = turtle.Turtle()
        self.runner.penup()
        self.runner.hideturtle()
        self.runner.shape('turtle')
        self.runner.color(color)
        self.runner.setpos(pos)


    def move(self):
        r = randrange(1,20)
        self.pos = (self.pos[0]+r, self.pos[1])
        self.runner.pendown()
        self.runner.forward(r)
    

def start_game():
    turtle.clearscreen()
    win.bgpic("./img/track.png")
    r_list = []

    colors = ['magenta', 'blue', 'green', 'red', 'purple', 'orange']
    y = 175

    # create runners
    for r in range(BOTS):
        y -= 50
        r_list.append(Racer(colors[r], (-175, y)))
        r_list[r].runner.showturtle()
        r_list[r].runner.setpos(-175,y)


    running = True
    winner_list = []
    while running:
        for r in r_list:
            r.move()
            for r in r_list:
                if r.pos[0] > 200:
                    winner_list.append(r)
                    r_list.remove(r)

        if len(r_list) == 0:
            running = False

    place = 1
    leaderboard = ''
    for w in winner_list:
        leaderboard += str(place) + "th place - " + w.color + "\n"
        place += 1

    leaderboard += "\n\n Do you want to play again?"
    play_again = tk.messagebox.askquestion("Result", leaderboard, icon='question')
    if play_again == 'yes':
        start_game()
    else:
        turtle.bye()



if __name__ == "__main__":
    win = Screen()
    win.setup(WIDTH, HEIGHT)
    win.title("Turtle Race")
    start_game()
    win.mainloop()




