################################################################################
################################################################################
################################################################################

import pygame, sys, threading, random, speech_recognition as sr;

################################################################################
################################################################################
################################################################################

from pygame.locals import *

################################################################################
################################################################################
################################################################################

# intialize pygame, recognizer, status code

pygame.init(); r = sr.Recognizer(); sc = 0

# sets appropriate caption for GUI window

pygame.display.set_caption("STT Demo GUI")

# open a window of the dimensions 960x480

scr = pygame.display.set_mode((960, 600))

################################################################################
################################################################################
################################################################################

colorA = (255, 0, 0)
colorB = (255, 255, 0, 122)
colorC = (0, 255, 0)
colkey = (127, 33, 33)

circleA = pygame.Surface((100, 100)) # 1st circle
circleB = pygame.Surface((100, 100)) # 2nd circle
circleC = pygame.Surface((100, 100)) # 3rd circle

circleA.fill(colkey); circleA.set_colorkey(colkey)
circleB.fill(colkey); circleB.set_colorkey(colkey)
circleC.fill(colkey); circleC.set_colorkey(colkey)

pygame.draw.circle(circleA, colorA, (50, 50), 50)
pygame.draw.circle(circleB, colorB, (50, 50), 50)
pygame.draw.circle(circleC, colorC, (50, 50), 50)

circleA.set_alpha(255)
circleB.set_alpha(255)
circleC.set_alpha(255)

################################################################################
################################################################################
################################################################################

start = pygame.image.load("fan.png") # image of the fan

angle = 0 # the angle of rotation increased from start

image = pygame.transform.rotate(start, angle) # rotated


font = pygame.font.SysFont('calibri', 16)

line1 = font.render("WARNING - only RED light will blink", 1, (0 ,0, 0))
line2 = font.render("DAZZLE  - all lights blink randomly", 1, (0 ,0, 0))
line3 = font.render("COOL ME - the fan will start spinning", 1, (0 ,0, 0))
line4 = font.render("Press ESC to cancel current operation", 1, (0 ,0, 0))
line5 = font.render("Press 'SpaceBar' key and speak any of the hotwords below", 1, (0 ,0, 0))
line6 = font.render("Listening ...", 1, (0 ,0, 0))

rect1 = line1.get_rect(); rect1.center = (480, 510)
rect2 = line2.get_rect(); rect2.center = (480, 530)
rect3 = line3.get_rect(); rect3.center = (480, 550)
rect4 = line4.get_rect(); rect4.topleft = (20, 20)
rect5 = line5.get_rect(); rect5.center = (480, 480)
rect6 = line6.get_rect(); rect6.bottomleft = (20, 580)

################################################################################
################################################################################
################################################################################

def clear_events():

    circleA.set_alpha(255)
    circleB.set_alpha(255)
    circleC.set_alpha(255)


    # clear the warning event from the queue
    
    pygame.time.set_timer(USEREVENT + 1, 0)

    # clear the dazzle event from the queue
    
    pygame.time.set_timer(USEREVENT + 2, 0)
    
################################################################################
################################################################################
################################################################################
    
def manage_state(spoke):

    global sc
    
    if spoke.lower() == "warning":

        sc = 1; clear_events() # clear the queue

        pygame.time.set_timer(USEREVENT + 1, 1000)


    if spoke.lower() == "dazzle":

        sc = 2; clear_events() # clear the queue

        pygame.time.set_timer(USEREVENT + 2, 250)
        

    if spoke.lower() == "call me":

        sc = 3; clear_events() # spins the fan

################################################################################
################################################################################
################################################################################

def warning_callback():

    # opacity value [0, 255]
    
    a = circleA.get_alpha()
    
    
    if a > 100:

        # now semi-transparent

        circleA.set_alpha(100)

    else:

        # make enitrely opaque

        circleA.set_alpha(255)

################################################################################
################################################################################
################################################################################

def dazzle_callback():

    
    # create a list of circle to iterate
    
    circles = (circleA, circleB, circleC)


    for c in circles:

        if random.randint(0, 1) == 0:

            c.set_alpha(255) # make opaque

        else:

            c.set_alpha(100) # semi-trans

################################################################################
################################################################################
################################################################################

def rot_center(image, rect, angle):

    # rotates the image according to the specified angle
    
    rot_image = pygame.transform.rotozoom(image, angle, 1)

    # the rectangle for the given image after its rotated
    
    rot_rect = rot_image.get_rect(center = rect.center)
    
    return rot_image,rot_rect # return both image and rect

################################################################################
################################################################################
################################################################################

def listen_stt():

    scr.blit(line6, rect6)

    pygame.display.flip()
    

    with sr.Microphone() as source:

        audio = r.listen(source) # listen
        
        spoke = r.recognize_google(audio)

        print spoke

        manage_state(spoke) # change state

################################################################################
################################################################################
################################################################################

while True:

    # refresh the screen
    
    pygame.display.flip()

    # gray color clear screen
    
    scr.fill((239, 239, 239))


    scr.blit(circleA, (180, 75))
    scr.blit(circleB, (430, 75))
    scr.blit(circleC, (680, 75))

    pygame.draw.circle(scr, (0, 0, 0), (230, 125), 55, 1)
    pygame.draw.circle(scr, (0, 0, 0), (480, 125), 55, 1)
    pygame.draw.circle(scr, (0, 0, 0), (730, 125), 55, 1)

    scr.blit(line1, rect1)
    scr.blit(line2, rect2)
    scr.blit(line3, rect3)
    scr.blit(line4, rect4)
    scr.blit(line5, rect5)


    if sc == 3:
        
        angle += 2 # increase angle
        

    oldRect = image.get_rect(center = (480, 350)) # old image

    image, rect = rot_center(start, oldRect, angle) # rotated

    scr.blit(image, rect) # rotate the image across its center  
        


    for event in pygame.event.get():
        
        if event.type == QUIT:

            # exit the whole program
            
            pygame.quit(); sys.exit()


        if event.type == USEREVENT + 1:

            warning_callback() # warning event
            

        if event.type == USEREVENT + 2:

            dazzle_callback() # a dazzle event
            

        if event.type == KEYDOWN:
            
            if event.key == K_SPACE:

                try:

                    listen_stt()

                except:

                    pass


            if event.key == K_ESCAPE:

                sc = 0; clear_events() # idle states

################################################################################
################################################################################
################################################################################
