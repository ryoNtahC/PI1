import pyglet
#konstanty okna
import pyglet.gl
from pyglet import gl

SIRKA = 1000
VYSKA = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST = 200 #pixely za sekundu

#palky
TLSTKA_PALKY = 10
VYSKA_PALKY = 200
RYCHLOST_PALKY = RYCHLOST * 1.5


#prostred naciata
CIARA_HRUBKA = 20

#font
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#stavove premenne
pozicie_palok = [VYSKA // 2, VYSKA//2]
pozicia_lopty = [SIRKA//2, VYSKA//2]
rychlost_lopty = [0, 0]
stisknutie_klaves = set()
skore = [0, 0]


def vykresli_obdlznik(x1,y1,x2,y2):
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku

def nakresli_text(text, x, y, pozice_x):
    napis = pyglet.text.Label(text,font_size=VELKOST_FONTU,x=x,y=y,anchor_x=pozice_x)
    napis.draw()

def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # zmaz obsah okna (vyfarbý na čierno)
    gl.glColor3f(1, 1, 1)


    #vykresli loptu
    vykresli_obdlznik(
        pozicia_lopty[0] - VELKOST_LOPTY //2,
        pozicia_lopty[1] - VELKOST_LOPTY //2,
        pozicia_lopty[0] + VELKOST_LOPTY //2,
        pozicia_lopty[1] + VELKOST_LOPTY //2

    )
    gl.glColor3f(255, 255, 1)
    vykresli_obdlznik(pozicia_lopty[0], pozicia_lopty[1], pozicia_lopty[0]+10, pozicia_lopty[1]+10)

    #vykresli palky
    for x, y in [(0, pozicie_palok[0]), (SIRKA, pozicie_palok[1])]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY//2,
            x + TLSTKA_PALKY,
            y + TLSTKA_PALKY//2

    )

    #Vykrelenie: Poliaca ciara
    for y in range (CIARA_HRUBKA // 2, VYSKA, CIARA_HRUBKA * 2):
        vykresli_obdlznik(
            SIRKA// 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + CIARA_HRUBKA
        )

    #vykresli skore

    nakresli_text(str(skore[0]),x=ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='left')
    nakresli_text(str(skore[1]),x=SIRKA-ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='right')


window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli
)

pyglet.app.run()


