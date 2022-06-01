import math
import random

import pyglet
from pyglet import gl
from pyglet.window import key

"---------Globalne konštanty a premenne----------"

"Window constants"
WIDTH = 1200
HEIGHT = 800

"Game constants"
ACCELERATION = 120              #Zrýchlenie rakety
ROTATION_SPEED = 0.05           #Rýchlosť otáčania rakety

game_objects = []
batch = pyglet.graphics.Batch() #ZOZNAM SPRITOV PRE ZJEDNODUŠENÉ VYKRESLENIE
pressed_keyboards = set()       #MNOŽINA ZMAČKNUTÝCH KLÁVES


SHOOT_DELAY = 0.5
LASER_SPEED = 275
LASER_LIFETIME = 45

SHIELD_ZIVOT = 3
POSITION_X = 0
POSITION_Y = 0
ROTATION = 0

ZIVOTY = 3

"Score"
score = 0
"------------------- FUNKCIE __________________"

"""
Vycentruj ukotvenie obrázka na stred
"""
def set_anchor_of_image_to_center(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

"""
Pomocna funkcia na zobrazenia kolizneho kolecka
"""
def draw_circle(x, y, radius):
    iterations = 20
    s = math.sin(2 * math.pi / iterations)
    c = math.cos(2 * math.pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_LINE_STRIP)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou
    for i in range(iterations + 1):
        gl.glVertex2f(x + dx, y + dy)
        dx, dy = (dx * c - dy * s), (dy * c + dx * s)
    gl.glEnd()


"----------------VLASTNÉ TRIEDY----------------"

"""
Rodičovská trieda
"""
class SpaceObject:
    "Konštruktor"
    def __init__(self, sprite, x, y, speed_x= 0, speed_y = 0):
        self.x_speed = speed_x
        self.y_speed = speed_y
        self.rotation = 1.57  # radiany -> smeruje hore

        self.sprite = pyglet.sprite.Sprite(sprite, batch=batch)
        self.sprite.x = x
        self.sprite.y = y
        self.radius = (self.sprite.height + self.sprite.width) // 4

    """
    Výpočet vzdialenosti medzi dvoma objektami
    Pytagorova veta
    """
    def distance(self, other):
        x = abs(self.sprite.x - other.sprite.x)
        y = abs(self.sprite.y - other.sprite.y)
        return (x**2 + y**2) ** 0.5 #pytagorova veta

    """
    Kolizná metóda s loďou - nie je nutné defunovať, 
    Definujeme až v odvodenej triede
    """
    def hit_by_spaceship(self, ship):
        pass

    """
    Kolízna metóda s laserom - nie je nutné defynovať
    Definujeme až v odvodenej triede
    """
    def hit_by_laser(self, laser):
        pass

    "Metoda ktora deletne objekt"
    def delete(self, dt =0 ):
        self.sprite.delete()
        game_objects.remove(self)

    """
    Metóda pre kontrolu pozície či sa nachádzame na okraji
    """
    def checkBoundaries(self):
        if self.sprite.x > WIDTH:
            self.sprite.x = 0

        if self.sprite.x < 0:
            self.sprite.x = WIDTH

        if self.sprite.y < 0:
            self.sprite.y = HEIGHT

        if self.sprite.y > HEIGHT:
            self.sprite.y = 0

    """
    Metoda tick spoločná pre všetky podtriedy
    """
    def tick(self, dt):
        "Posunutie vesmírnej lode na novú pozíciu"
        self.sprite.x += dt * self.x_speed
        self.sprite.y += dt * self.y_speed
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        "Kontrola či sme prešli kraj"
        self.checkBoundaries()

"""
Trieda Spaceship
Hlavný objekt hry, predstavuje hráča
"""
class Spaceship(SpaceObject):

    "Konśtruktor"
    def __init__(self, sprite, x ,y):
        super().__init__(sprite,x,y)
        self.laser_load = True
        self.shield = self.shield_on()
    """
    Metóda zodpovedná za vystrelenie laseru
    """
    def shoot(self):
        img = pyglet.image.load('Assetss\PNG\Lasers\laserBlue16.png')
        set_anchor_of_image_to_center(img)

        laser_x = self.sprite.x + math.cos(self.rotation) * self.radius
        laser_y = self.sprite.y + math.sin(self.rotation) * self.radius

        laser = Laser(img, laser_x, laser_y)
        laser.rotation = self.rotation

        game_objects.append(laser)


    """
    Každý frame sa vykoná táto metóda to znamená v našom prípade:
    60 simkov * za sekundu
    Mechanic of spaceship - rotation, movement, controls
    """
    def tick(self, dt):
        super().tick(dt)

        "Zrýchlenie po kliknutí klávesy W. Výpočet novej rýchlosti"
        if 'W' in pressed_keyboards:
            self.x_speed = self.x_speed + dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed = self.y_speed + dt * ACCELERATION * math.sin(self.rotation)

        "Spomalenie/spätný chod po kliknutí klávesy S"
        if 'S' in pressed_keyboards:
            self.x_speed = self.x_speed - dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed = self.y_speed - dt * ACCELERATION * math.sin(self.rotation)

        "Otočenie doľava - A"
        if 'A' in pressed_keyboards:
            self.rotation -= ROTATION_SPEED

        "Otočenie doprava - D"
        if 'D' in pressed_keyboards:
            self.rotation += ROTATION_SPEED

        "Ručná brzda - SHIFT"
        if 'SHIFT' in pressed_keyboards:
            self.x_speed = 0
            self.y_speed = 0

        "Steľba - SPACE"
        if "SPACE" in pressed_keyboards:
            self.shoot()
            self.laser_loaded = False
            pyglet.clock.schedule_once(self.reload_laser, SHOOT_DELAY)

        if self.shield == True:
            self.get_position()

        "VYBERIE VŠETKY OSTATNE OBJEKTY OKREM SEBA SAMA"
        for obj in [o for o in game_objects if o != self]:
            # d = distance medzi objektami
            d = self.distance(obj)
            if d < self.radius + obj.radius:
                obj.hit_by_spaceship(self)
                break

        self.get_position()


    "Metóda zodpovedná za reset pozície rakety"
    def reset(self):
        self.sprite.x = WIDTH // 2
        self.sprite.y = HEIGHT // 2
        self.rotation = 1.57  # radiany -> smeruje hore
        self.x_speed = 0
        self.y_speed = 0

    def laser_reload(self, dt):
        self.laser_load

    def get_position(self):
        global POSITIONX, POSITIONY, ROTATION
        POSITIONX = self.sprite.x
        POSITIONY = self.sprite.y
        ROTATION = self.rotation

    def shield_on(self):
        self.shield = True
        img = pyglet.image.load("Assetss/PNG/Effects/shield2.png")
        set_anchor_of_image_to_center(img)
        shield = Shield(img, self.sprite.x, self.sprite.y)

        game_objects.append(shield)
        pyglet.clock.schedule_once(self.shield_off, SHIELD_ZIVOT)
        self.get_position()

    def shield_off(self, dt):
        self.shield = False


"""
Trieda Asteroid
"""
class Asteroid(SpaceObject):
    "Metóda ktorá sa vykoná ak dôjde ku kolízii lode a asteroidu"
    def hit_by_spaceship(self, ship):
        global SHIELD_ZIVOT
        if ship.shield == False:
            pressed_keyboards.clear()
            ship.reset()
            ship.shield_on()
            ZIVOTY -= 1
        self.delete()

    "Metóda ktorá sa vykoná ak dôjde ku kolízii a asteroidu"
    def hit_by_laser(self, laser):
        global score
        self.delete()
        laser.delete()
        score += 100

"""
Trieda Laser
"""
class Laser(SpaceObject):
    def __int__(self, sprite, x, y):
        super().__int__(sprite, x, y)
        self.laserlifetime = LASER_LIFETIME


    def tick(self, dt):
        super().tick(dt)
        self.laserlifetime -= 0.5
        if self.laserlifetime == 0:
            self.delete()

        self.x_speed = LASER_SPEED = math.cos(self.rotation)
        self.y_speed = LASER_SPEED = math.sin(self.rotation)

        for obj in [o for o in game_objects if o != self and o != Spaceship]:
            dis = self.distance(obj)
            if dis < self.radius + obj.radius:
                obj.hit_by_laser(self)
                break

class Shield(SpaceObject):
    def __init__(self, sprite, x, y):
        super().__init__(sprite, x, y)
        self.shield_life = SHIELD_ZIVOT

    def tick(self, dt):
        global position_x, position_y, rotation
        super().tick(dt)

        self.sprite.x = POSITION_X
        self.sprite.y = POSITION_Y
        self.rotation = ROTATION

        self.shield_life -= dt
        if self.shield_life <=0:
            self.delete()


"""
GAME WINDOW CLASS
"""
class Game:
    """
    Konstruktor
    """
    def __init__(self):
        self.window = None
        game_objects = []

    """
    Načítanie všetkých spritov
    """
    def load_resources(self):
        self.playerShip_image = pyglet.image.load('Assetss/PNG/playerShip1_blue.png')
        set_anchor_of_image_to_center(self.playerShip_image)
        self.background_image = pyglet.image.load('Assetss/Backgrounds/black.png')
        self.asteroid_images = ['Assetss/PNG/Meteors/meteorGrey_big1.png',
                           'Assetss/PNG/Meteors/meteorGrey_med1.png',
                           'Assetss/PNG/Meteors/meteorGrey_small1.png',
                           'Assetss/PNG/Meteors/meteorGrey_tiny1.png']
        self.ship_life_image = pyglet.image.load('Assetss/PNG/UI/playerLife1_blue.png')

        def ship_life(self):
            for i in range(ZIVOTY):
                self.ship_life_image.blit(30 + i * 35, 30)
            sprite = pyglet.sprite.Sprite(self.ship_life_image, batch=batch)


    """
    Vytvorenie objektov pre začiatok hry
    """
    def init_objects(self):
        #Vytvorenie lode
        spaceShip = Spaceship(self.playerShip_image, WIDTH // 2, HEIGHT//2)
        game_objects.append(spaceShip)

        #Nastavenie pozadia a prescalovanie
        self.background = pyglet.sprite.Sprite(self.background_image)
        self.background.scale_x = 6
        self.background.scale_y = 4

        #Vytvorenie Meteoritov
        self.create_asteroids(count=7)
        #Pridavanie novych asteroidoch každych 10 sekund
        pyglet.clock.schedule_interval(self.create_asteroids, 10, 1)

    def create_asteroids(self, dt=0, count=1):
        "Vytvorenie X asteroidov"
        for i in range(count):
            # Výber asteroidu náhodne
            img = pyglet.image.load(random.choice(self.asteroid_images))
            set_anchor_of_image_to_center(img)

            # Nastavenie pozície na okraji obrazovky náhodne
            position = [0, 0]
            dimension = [WIDTH, HEIGHT]
            axis = random.choice([0, 1])
            position[axis] = random.uniform(0, dimension[axis])

            # Nastavenie rýchlosti
            tmp_speed_x = random.uniform(-100, 100)
            tmp_speed_y = random.uniform(-100, 100)

            #Temp asteroid object
            asteroid = Asteroid(img, position[0], position[1], tmp_speed_x, tmp_speed_y)
            game_objects.append(asteroid)

    """
    Event metóda ktorá sa volá na udalosť on_draw stále dookola
    """
    def draw_game(self):
        # Vymaže aktualny obsah okna
        self.window.clear()
        # Vykreslenie pozadia
        self.background.draw()
        scoreLabel = pyglet.text.Label(text=str(score), font_size=40, x=1150, y=760, anchor_x='right',anchor_y='center')
        scoreLabel.draw()

        self.ship_life()

        "Vykreslenie koliznych koliečok"
        for o in game_objects:
            draw_circle(o.sprite.x, o.sprite.y, o.radius)

        # Táto časť sa stará o to aby bol prechod cez okraje okna plynulý a nie skokový
        for x_offset in (-self.window.width, 0, self.window.width):
            for y_offset in (-self.window.height, 0, self.window.height):
                # Remember the current state
                gl.glPushMatrix()
                # Move everything drawn from now on by (x_offset, y_offset, 0)
                gl.glTranslatef(x_offset, y_offset, 0)

                # Draw !!! -> Toto vykreslí všetky naše sprites
                batch.draw()

                # Restore remembered state (this cancels the glTranslatef)
                gl.glPopMatrix()

    """
    Event metóda pre spracovanie klávesových vstupov
    """
    def key_press(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.add('W')
        if symbol == key.S:
            pressed_keyboards.add('S')
        if symbol == key.A:
            pressed_keyboards.add('A')
        if symbol == key.D:
            pressed_keyboards.add('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.add('SHIFT')
        if symbol == key.SPACE:
            pressed_keyboards.add("SPACE")

    """
    Event metóda pre spracovanie klávesových výstupov
    """
    def key_release(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.discard('W')
        if symbol == key.S:
            pressed_keyboards.discard('S')
        if symbol == key.A:
            pressed_keyboards.discard('A')
        if symbol == key.D:
            pressed_keyboards.discard('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.discard('SHIFT')
        if symbol == key.SPACE:
            pressed_keyboards.discard("SPACE")

    """
    Update metóda
    """
    def update(self, dt):
        for obj in game_objects:
            obj.tick(dt)

    """
    Start game metóda 
    """
    def start(self):
        "Vytvorenie hlavneho okna"
        self.window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

        "Nastavenie udalosti (eventov)"
        self.window.push_handlers(
            on_draw=self.draw_game,
            on_key_press=self.key_press,
            on_key_release=self.key_release
        )

        "Load resources"
        self.load_resources()

        "Inicializacia objektov"
        self.init_objects()

        "Nastavenie timeru pre update metódu v intervale 1./60 = 60FPS"
        pyglet.clock.schedule_interval(self.update, 1. / 60)

        pyglet.app.run()  # all is set, the game can start

"----------- StartGame -----------"
Game().start()



