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
# Lets you change speed of all players, once there is more than one


#Loading Sprites
walkRight = pg.image.load("R1.png")
walkLeft = pg.image.load("L1.png")
walkUp = pg.image.load("U1.png")
walkDown = pg.image.load("D1.png")

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


def redrawGameWindow():
    screen.blit(background, (0, 0))
    screen.blit(overground, (0, 0))
    #Runs draw method from player class:
    P1.draw(screen)
    P2.draw(screen)
    pg.display.update()

# Creates Player 1 Object
P1 = player(65, 400, 34, 56)
P2 = player(115, 400, 34, 56)
run = True
while run:
    pg.time.delay(10)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    P1key = pg.key.get_pressed()
    P2key = pg.key.get_pressed()
    if P1key[pg.K_LEFT] and P1.x > P1.vel: 
        P1.x-= P1.vel
        P1.left = True
        P1.right = False
        P1.up = False
        P1.down = False

    if P1key[pg.K_RIGHT] and P1.x < screenWidth - P1.width - P1.vel: 
        P1.x+= P1.vel
        P1.left = False
        P1.right = True
        P1.up = False
        P1.down = False

    if P1key[pg.K_UP] and P1.y > P1.vel: 
        P1.y-= P1.vel
        P1.left = False
        P1.right = False
        P1.up = True
        P1.down = False
        
    if P1key[pg.K_DOWN] and P1.y < screenWidth - P1.height - P1.vel:
        P1.y += P1.vel
        P1.left = False
        P1.right = False
        P1.up = False
        P1.down = True

    # Player 2
    if P2key[pg.K_a] and P2.x > P2.vel: 
        P2.x-= P2.vel
        P2.left = True
        P2.right = False
        P2.up = False
        P2.down = False

    if P2key[pg.K_d] and P2.x < screenWidth - P2.width - P2.vel: 
        P2.x+= P2.vel
        P2.left = False
        P2.right = True
        P2.up = False
        P2.down = False

    if P2key[pg.K_w] and P2.y > P2.vel: 
        P2.y-= P2.vel
        P2.left = False
        P2.right = False
        P2.up = True
        P2.down = False
        
    if P2key[pg.K_s] and P2.y < screenWidth - P2.height - P2.vel:
        P2.y += P2.vel
        P2.left = False
        P2.right = False
        P2.up = False
        P2.down = True
    redrawGameWindow()
pg.quit()