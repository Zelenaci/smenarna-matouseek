import pygame as tkinter
import sys as sus

class Window:
    def __init__(self):

        tkinter.init()
        self.win = tkinter.display.set_mode((250, 550))

        self.gray = (220,220,220)
        self.black = (0,0,0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.purple = (75, 0, 130)

        self.clock = tkinter.time.Clock()

        self.font = None
        self.text = None
        self.textRect = None

        self.input_box = tkinter.Rect(5, 435, 140, 32)
        self.color_inactive = (255, 0, 0)
        self.color_active = (0, 255, 0)
        self.color = self.color_inactive
        self.active = False
        self.textInput = ''

        self.nakup = None
        self.prodej = None
        self.eur = None
        self.gbp = None
        self.usd = None
        self.jpy = None
        self.cad = None

        self.colorNakup = self.color_inactive
        self.activeNakup = False
        self.colorProdej = self.color_inactive
        self.activeProdej = False

        self.KolikKupujes = 1
        self.ZaKolik = 1
        self.KolikChci = 1
        self.finalniCena = None

        self.indexProdej = 3
        self.indexNakup = 4
        
        self.listek = []

        with open('listek.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                txt = line.split()
                self.listek.append(txt)

    def check_events(self):
        for event in tkinter.event.get():
            if event.type == tkinter.QUIT:
                tkinter.quit()
                sus.exit()
            if event.type == tkinter.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

                if self.active:
                    self.color = self.color_active
                else:
                    self.color = self.color_inactive


                if self.nakup.collidepoint(event.pos):
                    self.activeNakup = True
                    self.activeProdej = False
                    self.colorNakup = self.color_active
                    self.colorProdej = self.color_inactive


                if self.prodej.collidepoint(event.pos):
                    self.activeProdej = True
                    self.activeNakup = False
                    self.colorProdej = self.color_active
                    self.colorNakup = self.color_inactive



                if self.eur.collidepoint(event.pos):
                    self.KolikKupujes = self.listek[0][1]
                    self.KolikChci = 0
                    if self.activeNakup:
                        self.ZaKolik = self.listek[0][3]
                    else:
                        self.ZaKolik = self.listek[0][2]

                if self.gbp.collidepoint(event.pos):
                    self.KolikKupujes = self.listek[1][1]
                    self.KolikChci = 0
                    if self.activeNakup:
                        self.ZaKolik = self.listek[1][3]
                    else:
                        self.ZaKolik = self.listek[1][2]

                if self.usd.collidepoint(event.pos):
                    self.KolikKupujes = self.listek[2][1]
                    self.KolikChci = 0
                    if self.activeNakup:
                        self.ZaKolik = self.listek[2][3]
                    else:
                        self.ZaKolik = self.listek[2][2]

                if self.jpy.collidepoint(event.pos):
                    self.KolikKupujes = self.listek[3][1]
                    self.KolikChci = 0
                    if self.activeNakup:
                        self.ZaKolik = self.listek[3][3]
                    else:
                        self.ZaKolik = self.listek[3][2]

                if self.cad.collidepoint(event.pos):
                    self.KolikKupujes = self.listek[4][1]
                    self.KolikChci = 0
                    if self.activeNakup:
                        self.ZaKolik = self.listek[4][3]
                    else:
                        self.ZaKolik = self.listek[4][2]
            
            if event.type == tkinter.KEYDOWN:
                if self.active:
                    if event.key == tkinter.K_RETURN:
                        self.KolikChci = self.textInput
                        self.textInput = ''
                    elif event.key == tkinter.K_BACKSPACE:
                        self.textInput = self.textInput[:-1]
                    else:
                        self.textInput += event.unicode
                    
                    if len(self.textInput) > 9:
                        self.textInput = ''

    def loop(self):
        while True:
            self.clock.tick(60)
            self.win.fill(self.gray)

            tkinter.draw.rect(self.win, self.color, self.input_box, 2)
            self.draw_text(self.textInput, 20, 75, 450, self.color)

            self.check_events()

            tkinter.draw.rect(self.win, (255, 50, 50), (0, 0, 245, 545), 4)

            self.draw_text('Smenarna', 25, 125, 25, self.black)

            self.draw_text('Transakce', 23, 60, 50, self.black)
            self.nakup = self.draw_text('Nakup', 20, 60, 75, self.colorNakup)
            self.prodej = self.draw_text('Prodej', 20, 60, 105, self.colorProdej)

            self.draw_text('Mena', 23, 60, 140, self.black)
            self.eur = self.draw_text('EUR', 20, 60, 165, self.red)
            self.gbp = self.draw_text('GBP', 20, 60, 195, self.red)
            self.usd = self.draw_text('USD', 20, 60, 225, self.red)
            self.jpy = self.draw_text('JPY', 20, 60, 255, self.red)
            self.cad = self.draw_text('CAD', 20, 60, 285, self.red)

            self.draw_text('Kurz', 23, 60, 320, self.black)
            self.draw_text(str(self.KolikKupujes), 20, 60, 345, self.purple)
            self.draw_text(str(self.ZaKolik), 20, 60, 375, self.purple)

            self.draw_text('Vypocet', 23, 60, 410, self.black)

            try:
                self.finalniCena = (float(self.KolikChci)/float(self.KolikKupujes))*float(self.ZaKolik)
            except:
                self.finalniCena = 'Nevalidni hodnota'

            self.draw_text(str(self.finalniCena), 20, 60, 480, self.purple)

            tkinter.display.update()
    
    def draw_text(self, text, size, x, y, text_color):
        self.font = tkinter.font.SysFont('notoserif', size)
        self.text = self.font.render(text, True, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.win.blit(self.text, self.textRect)
        return self.textRect

win = Window()
win.loop()