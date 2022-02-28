import pygame as tkinter
import sys as sus

class Window:
    def __init__(self):
        tkinter.init()
        self.win = tkinter.display.set_mode((250, 550))
        self.gray = (220,220,220)
        self.black = (0,0,0)
        self.font = None
        self.text = None
        self.textRect = None

    def check_events(self):
        for event in tkinter.event.get():
            if event.type == tkinter.QUIT:
                tkinter.quit()
                sus.exit()

    def loop(self):
        while True:
            self.win.fill(self.gray)
            self.check_events()

            tkinter.draw.rect(self.win, (255, 50, 50), (0, 0, 245, 545), 4)

            self.draw_text('transakce', 25, 150, 150, self.black)

            tkinter.display.update()
    
    def draw_text(self, text, size, x, y, text_color):
        self.font = tkinter.font.Font('lato', size)
        self.text = self.font.render(text, True, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.win.blit(self.text, self.textRect)
        return self.textRect

win = Window()
win.loop()