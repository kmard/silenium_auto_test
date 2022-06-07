# https://python-scripts.com/category/gui/tkinter-python

from tkinter import *

import PIL.Image
from PIL import Image, ImageTk

import random

WIDTH = 1000
HEIGHT = 900
BODYSIZE = 50
STARTDELAY = 500
MINDELAY = 100
STEPDELAY = 20
LENGHT = 3

countBodyW = WIDTH / BODYSIZE
countBodyH = HEIGHT / BODYSIZE

x = [0] * int(countBodyW)
y = [0] * int(countBodyH)


def setwindow(root):
    root.title("Snail")
    root.board = Snake()

    root.resizable(False, False)

    # w = root.winfo_reqwidth()
    # h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - WIDTH / 2)
    y = int(wh / 2 - HEIGHT / 2)

    root.geometry("+{0}+{1}".format(x, y))


class Snake(Canvas):
    headImage = False
    head = False
    body = False
    apple = False
    delay = 0
    direction = 'Right'
    directiontemp = 'Right'
    loss = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background='black', highlightthickness=0)
        self.focus()
        self.bind_all('<Key>', self.onKeyPressed)
        self.loadResources()
        self.beginplay()
        self.pack()

    def loadResources(self):
        self.headImage = Image.open(r'C:\Projects_Python\Rusak\snake\head.png')

        self.head = ImageTk.PhotoImage(self.headImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(Image.open(r'C:\Projects_Python\Rusak\snake\body.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.apple = ImageTk.PhotoImage(Image.open(r'C:\Projects_Python\Rusak\snake\apple.png').resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))


    def beginplay(self):
        self.delay = STARTDELAY
        self.direction = 'Right'
        self.directiontemp = 'Right'
        self.loss = False

        self.delete(ALL)
        self.spawnActors()
        self.after(self.delay,self.timer)

    def spawnActors(self):

        self.spawnApple()

        x[0] = int(countBodyW / 2) * BODYSIZE
        y[0] = int(countBodyH / 2) * BODYSIZE
        for i in range(1, LENGHT):
            x[i] = x[0] - BODYSIZE * i
            y[i] = y[0]
        self.create_image(x[0], y[0], image=self.head, anchor='nw', tag='head')
        for i in range(LENGHT - 1, 0, -1):
            self.create_image(x[i], y[i], image=self.body, anchor='nw', tag='body')


    def spawnApple(self):
        apple = self.find_withtag('apple')
        if apple:
            self.delete(apple[0])
        rx = random.randint(0, countBodyW - 1)
        ry = random.randint(0, countBodyH - 1)
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, anchor='nw', image=self.apple, tag='apple')

    def checkApple(self):
        apple = self.find_withtag('apple')[0]
        head = self.find_withtag('head')
        x1, y1, x2, y2 = self.bbox(head)
        overlaps = self.find_overlapping(x1, y1, x2, y2)
        for actor in overlaps:
            if actor == apple:
                tempx,tempy = self.coords(apple)
                self.spawnApple()
                self.create_image(tempx,tempy,image=self.body,anchor='nw', tag='body')
                if self.delay > MINDELAY:
                    self.delay-=STEPDELAY

    def checkCollisions(self):
        head = self.find_withtag('head')
        body = self.find_withtag('body')
        x1, y1, x2, y2 = self.bbox(head)
        overlaps = self.find_overlapping(x1, y1, x2, y2)
        for b in body:
            for actor in overlaps:
                if actor == b:
                    self.loss = True
        if x1 < 0:
            self.loss = True
        if x2 > WIDTH:
            self.loss = True
        if y1 < 0:
            self.loss = True
        if y2 > HEIGHT:
            self.loss = True


    def onKeyPressed(self, event):
        key = event.keysym
        if key == 'Left' and self.direction != 'Right':
            self.directiontemp = key
        elif key == 'Right' and self.direction != 'Left':
            self.directiontemp = key
        elif key == 'Up' and self.direction != 'Down':
            self.directiontemp = key
        elif key == 'Down' and self.direction != 'Up':
            self.directiontemp = key
        elif key == 'space' and self.loss:
            self.beginplay()



    def updateDirection(self):
        self.direction = self.directiontemp
        head = self.find_withtag('head')
        headx, heady = self.coords(head)
        self.delete(head)
        if self.direction == 'Left':
            self.head = ImageTk.PhotoImage(self.headImage.transpose(Image.FLIP_LEFT_RIGHT).resize((BODYSIZE,BODYSIZE),Image.ANTIALIAS))
        else:
            rotates = {'Right': 0, 'Up': 90, 'Down': -90}
            self.head = ImageTk.PhotoImage(self.headImage.rotate(rotates[self.direction]).resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

        self.create_image(headx, heady, image=self.head, anchor='nw', tag='head')



    def timer(self):
        self.checkCollisions()
        # print(self.loss)
        if not self.loss:
            self.checkApple()
            self.updateDirection()
            self.moveSnake()
            self.after(self.delay, self.timer)
        else:
            self.gameOver()

    def moveSnake(self):
        head = self.find_withtag('head')
        body = self.find_withtag('body')
        items = body+head
        for i in range(len(items)-1):
            currentxy = self.coords(items[i])
            nextxy = self.coords(items[i + 1])
            self.move(items[i], nextxy[0] - currentxy[0], nextxy[1] - currentxy[1])
        if self.direction == 'Left':
            self.move(head, -BODYSIZE, 0)
        elif self.direction == 'Right':
            self.move(head, BODYSIZE, 0)
        elif self.direction == 'Up':
            self.move(head, 0, -BODYSIZE)
        elif self.direction == 'Down':
            self.move(head, 0, BODYSIZE)

    def gameOver(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2-60,text='Game over', fill='white', font='Tahoma 40', tag='text')
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2+60,text='Push Shift for new game', fill='white', font='Tahoma 40', tag='text')



root = Tk()
setwindow(root)

root.mainloop()