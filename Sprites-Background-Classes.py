# links:
# https://stackoverflow.com/questions/60387843/having-a-sprite-follow-a-line-of-a-specific-color-pygame
import pygame as pg
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

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def draw(self, screen) : 
        if self.left == True:
            screen.blit(walkLeft, (self.x,self.y))    
        elif self.right == True:
            screen.blit(walkRight, (self.x,self.y))
        elif self.up == True:
            screen.blit(walkUp, (self.x,self.y))
        elif self.down == True:
            screen.blit(walkDown, (self.x,self.y))
        #else:
            #screen.blit(walkRight, (x,y))

#Loading Sprites
walkRight = pg.image.load("R1.png")
walkLeft = pg.image.load("L1.png")
walkUp = pg.image.load("U1.png")
walkDown = pg.image.load("D1.png")

def redrawGameWindow():
    screen.blit(background, (0, 0))
    screen.blit(overground, (0, 0))
    #Runs draw method from player class:
    P1.draw(screen)
    
    pg.display.update()

# Creates Player 1 Object
P1 = player(20, 400, 34, 56)
run = True
while run:
    pg.time.delay(100)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and P1.x > P1.vel: 
        P1.x-= P1.vel
        P1.left = True
        P1.right = False
        P1.up = False
        P1.down = False

    if keys[pg.K_RIGHT] and P1.x < screenWidth - P1.width - P1.vel: 
        P1.x+= P1.vel
        P1.left = False
        P1.right = True
        P1.up = False
        P1.down = False

    if keys[pg.K_UP] and P1.y > P1.vel: 
        P1.y-= P1.vel
        P1.left = False
        P1.right = False
        P1.up = True
        P1.down = False
        
    if keys[pg.K_DOWN] and P1.y < screenWidth - P1.height - P1.vel:
        P1.y += P1.vel
        P1.left = False
        P1.right = False
        P1.up = False
        P1.down = True
    #else:
       # left = False
       # right = False
       # up = False
       # down = False
    redrawGameWindow()
pg.quit()