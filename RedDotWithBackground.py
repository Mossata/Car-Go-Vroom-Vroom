import pygame as pg
#b5f447 - number for green
pg.init() 
screen = pg.display.set_mode((1370, 700))
pg.display.set_caption("First Game")
screenWidth = 1370
x = 20 
y = 440
width = 34
height = 56
vel = 10
left = False
right = False
up = False
down = False

#Current images do not work, need to find compatible sprites
walkRight = pg.image.load("R1.png")
walkLeft = pg.image.load("L1.png")
walkUp = pg.image.load("U1.png")
walkDown = pg.image.load("D1.png")
background = pg.image.load('racetrack.PNG')

def redrawGameWindow():
    background = pg.transform.smoothscale(pg.image.load("racetrack.PNG"), (1370,700))
    # Reformats background image to fit screen size
    screen.blit(background, (0, 0))
    if left == True:
        screen.blit(walkLeft, (x,y))    
    elif right == True:
        screen.blit(walkRight, (x,y))
    elif up == True:
        screen.blit(walkUp, (x,y))
    elif down == True:
        screen.blit(walkDown, (x,y))
    #else:
       # screen.blit(walkRight, (x,y))
    
    pg.display.update()


run = True
while run:
    pg.time.delay(100)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > vel: 
        x-= vel
        left = True
        right = False
        up = False
        down = False

    if keys[pg.K_RIGHT] and x < screenWidth - width - vel: 
        x+= vel
        left = False
        right = True
        up = False
        down = False

    if keys[pg.K_UP] and y > vel: 
        y-= vel
        left = False
        right = False
        up = True
        down = False
        
    if keys[pg.K_DOWN] and y < screenWidth - height - vel:
        y += vel
        left = False
        right = False
        up = False
        down = True
    #else:
       # left = False
       # right = False
       # up = False
       # down = False
    redrawGameWindow()
pg.quit()