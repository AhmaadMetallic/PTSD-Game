import pygame
import time
import random
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.mixer.music.load('The_Lessondary_-_04_-_PTSD.ogg')


while mixer.music.get_busy():
    time.clock().tick(10)
        
display_width = 1280
display_height = 760

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (171, 208, 188)

bright_red = (255, 38, 38)
gray = (63, 63, 63)

car_width = 143                 

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PTSD Game')
clock = pygame.time.Clock()

bg = pygame.image.load('cityscape_no-church.png')
elucidImg = pygame.image.load('elucid.png')
pillsImg = pygame.image.load('pills.png')
drinkImg = pygame.image.load('drink.png')
weedImg = pygame.image.load('weed.png')
lsndryImg = pygame.image.load('Lessondary-Logo-Black-web-transparent.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: '+str(count), True, white)
    gameDisplay.blit(text, (0,0))  

def pills(pillsx, pillsy, pillsw, pillsh): 
    gameDisplay.blit(pillsImg,[pillsx, pillsy, pillsw, pillsh])

def drink(drinkx, drinky, drinkw, drinkh): 
    gameDisplay.blit(drinkImg,[drinkx, drinky, drinkw, drinkh])

def weed(weedx, weedy, weedw, weedh): 
    gameDisplay.blit(weedImg,[weedx, weedy, weedw, weedh])

def elucid(x,y):
    gameDisplay.blit(elucidImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
     

def crash():
    message_display('You Lose')

def button(msg,x,y,w,h,ic,ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "PLAY":
                  game_loop()
        elif action == "QUIT":
            pygame.quit()
            quit()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

    

def game_intro():
    pygame.mixer.music.play(-2)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(green)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("PTSD", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY",500,450,100,50, red, bright_red, "PLAY")       
        button("QUIT",680,450,100,50, black, gray, "QUIT")

        
        pygame.display.update()
        clock.tick(15)
        
        


def game_loop():
    gameDisplay.blit(bg, (0,0))

    
    x = (display_width * 0.45)
    y = (display_height * 0.5)

    x_change = 0

    pills_startx = random.randrange(0,display_width)
    pills_starty = -600
    pills_speed = 4
    pills_width = 60
    pills_height = 43

    drink_startx = random.randrange(0,display_width)
    drink_starty = -1200
    drink_speed = 4
    drink_width = 133
    drink_height = 211

    weed_startx = random.randrange(0,display_width)
    weed_starty = -1800
    weed_speed = 4
    weed_width = 91
    weed_height = 91
    

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change      
        gameDisplay.blit(bg, (0,0))


        #pills(pillsx, pillsy, pillsw, pillsh, color:)
        pills(pills_startx, pills_starty, pills_width, pills_height)
        pills_starty += pills_speed
        elucid (x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if pills_starty > display_height:
            pills_starty = 0 - pills_height
            pills_startx = random.randrange (0,display_width)
            dodged += 1
            pills_speed += .5
            

        if y < pills_starty+pills_height:
            print('y crossover')

            if x > pills_startx and x < pills_startx + pills_width or x + car_width > pills_startx and x + car_width < pills_startx + pills_width:
                print ('x crossover')
                crash()

        #drink(drinkx, drinky, drinkw, drinkh, color:)
        drink(drink_startx, drink_starty, drink_width, drink_height)
        drink_starty += drink_speed
        elucid (x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if drink_starty > display_height:
            drink_starty = 0 - drink_height
            drink_startx = random.randrange (0,display_width)
            dodged += 1
            drink_speed += .5
            

        if y < drink_starty+drink_height:
            print('y crossover')

            if x > drink_startx and x < drink_startx + drink_width or x + car_width > drink_startx and x + car_width < drink_startx + drink_width:
                print ('x crossover')
                crash()

        #weed(weedx, weedy, weedw, weedh, color:)
        weed(weed_startx, weed_starty, weed_width, weed_height)
        weed_starty += weed_speed
        elucid (x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if weed_starty > display_height:
            weed_starty = 0 - weed_height
            weed_startx = random.randrange (0,display_width)
            dodged += 1
            weed_speed += .5
            

        if y < weed_starty+drink_height:
            print('y crossover')

            if x > weed_startx and x < weed_startx + weed_width or x + car_width > weed_startx and x + car_width < weed_startx + weed_width:
                print ('x crossover')
                crash()
            
                    
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()


    
