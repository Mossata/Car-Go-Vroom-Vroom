# links:
# https://stackoverflow.com/questions/60387843/having-a-sprite-follow-a-line-of-a-specific-color-pygame
import pygame as pg
import math
#83b925 - number for green
#7f7f7f - number for grey

#Loading Backgrounds
pg.init() 
background = pg.transform.smoothscale(pg.image.load("green.png"), (1370,710))
bg_size = background.get_size()
screen = pg.display.set_mode(bg_size)
screen.blit(background, (0, 0))
overground = pg.transform.smoothscale(pg.image.load("track.png"), (1370,710))
track_size = overground.get_size()
track = pg.display.set_mode(track_size)
pg.display.set_caption("First Game")

screenWidth = 1370
vel = 5
still = pg.image.load("U1.png")

#Loading Sprites
Car = pg.image.load("U1.png")

def convertRadian (bearing):
        return bearing * (math.pi / 180)

class player():
    def __init__(self, x, y, width, height, bearing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.rotated_img = still
        self.bearing = 0
        self.AtH = 0
        self.dx = 0
        self.dy = 0
        self.left = False
        self.right = False
        self.up = False
        

    def rotate(self, screen) : 
        global Car
        pos = (self.x, self.y)
        #Calculating Box size of image
        w, h = Car.get_size()
        box = [pg.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.bearing) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        #Calculating Pivot Point
        pivot = pg.math.Vector2(w/2, -h/2)
        pivot_rotate = pivot.rotate(self.bearing)
        pivot_move  = pivot_rotate - pivot

        origin = (pos[0] + min_box[0] - pivot_move[0], pos[1] - max_box[1] + pivot_move[1])

        if self.left == True:
            self.rotated_img = pg.transform.rotate(Car, self.bearing)
            self.bearing = (self.bearing + 4) % 360
            screen.blit(self.rotated_img, origin)    

        elif self.right == True:
            self.rotated_img = pg.transform.rotate(Car, self.bearing)
            self.bearing = (self.bearing - 4) % 360
            screen.blit(self.rotated_img, origin)    

        else:
            screen.blit(self.rotated_img, origin)
        
        self.left = False
        self.right = False
        
        pg.display.update()

    def findChange (self):
        # returns an x and y change
        if self.bearing == 0: 
            return (0, - self.vel)
        elif self.bearing == 90:
            return (-self.vel, 0)
        elif self.bearing == 180:
            return (0, self.vel)
        elif self.bearing == 270:
            return (-self.vel, 0)
        
        elif self.bearing < 90:
           # print('Q1')
            return (math.sin(convertRadian(self.bearing)) * self.vel, math.cos(convertRadian(self.bearing)) * -self.vel)
        elif self.bearing < 180: 
           # print('Q2')
            self.AtH = self.bearing - 90
            return (math.cos(convertRadian(self.AtH)) * self.vel, math.sin(convertRadian(self.AtH)) * self.vel)
        elif self.bearing < 270:
           # print('Q3')
            self.AtH = 270 - self.bearing
            return (math.cos(convertRadian(self.AtH)) * -self.vel, math.sin(convertRadian(self.AtH)) * self.vel)
        elif self.bearing < 360:
            #print('Q4')
            self.AtH = self.bearing - 270
            return (math.cos(convertRadian(self.AtH)) * -self.vel, math.sin(convertRadian(self.AtH)) * -self.vel)
            
    def moveCar(self, dx, dy):
        pos = (self.x, self.y)
        #Calculating Box size of image
        w, h = Car.get_size()
        box = [pg.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.bearing) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        #Calculating Pivot Point
        pivot = pg.math.Vector2(w/2, -h/2)
        pivot_rotate = pivot.rotate(self.bearing)
        pivot_move  = pivot_rotate - pivot

        origin = (pos[0] + min_box[0] - pivot_move[0], pos[1] - max_box[1] + pivot_move[1])

        self.x += -self.dx
        self.y += self.dy
        screen.blit(self.rotated_img, origin)
        


def movement(Player1, Player2, noInput):
    P1.dx, P1.dy = 0, 0 
    P2.dx, P2.dy = 0, 0
    # Find change is pos with findChange then move car with change in pos
    if Player1 == True:
        P1.dx, P1.dy = P1.findChange()
        P1.moveCar(P1.dx, P1.dy)
        Player1 = False
    if Player2== True:
        P2.dx, P2.dy = P2.findChange()
        P2.moveCar(P2.dx, P2.dy)
        Player2 = False
    if noInput == True:
        P1.moveCar(P1.dx, P1.dy)
        P2.moveCar(P1.dx, P1.dy)
        noInput = False
    pg.display.update()

# Creates Player 1 Object
P1 = player(65, 400, 34, 56, 0)
P2 = player(115, 400, 34, 56, 0)
run = True
while run:
    pg.time.delay(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.blit(background, (0, 0))
    screen.blit(overground, (0, 0))

    P1key = pg.key.get_pressed()
    P2key = pg.key.get_pressed()

    # Player 1
    if P1key[pg.K_LEFT]:
        P1.left = True
        P1.rotate(screen)

    if P1key[pg.K_RIGHT]:
        P1.right = True
        P1.rotate(screen)

    if P1key[pg.K_UP]:
        movement(True, False, False)

    # Player 2
    if P2key[pg.K_a]:
        P2.left = True
        P2.rotate(screen)

    if P2key[pg.K_d]:
        P2.right = True
        P2.rotate(screen)
    
    if P2key[pg.K_w]:
        movement(False, True, False)
    
    else:
        movement(False, False, True)

    pg.display.update()

pg.quit()